from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render

from .forms import ContactForm
from .models import ContactInfo


def contact(request):
    contact_info = ContactInfo.objects.last()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            to_send = contact_info.email

            # Envía el correo electrónico
            try:
                send_mail(
                    subject,
                    f"Mensaje de {name} ({email}):\n\n{message}",
                    settings.DEFAULT_FROM_EMAIL,  # Usar el correo por defecto de settings
                    [to_send],  # Receptor del mensaje
                    fail_silently=False,
                )
                response = {"success": True}
            #                return HttpResponse("Mensaje enviado con éxito.")
            except Exception as e:
                response = {"success": False, "error": str(e)}
            #                return HttpResponse(f"Error al enviar el mensaje: {e}")
            return JsonResponse(response)
    else:
        form = ContactForm()

    return render(
        request, "contact/contact.html", {"form": form, "contact_info": contact_info}
    )
