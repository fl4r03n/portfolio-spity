from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Envía el correo electrónico
            send_mail(
                subject,
                f"Mensaje de {name} ({email}):\n\n{message}",
                email,
                ["flareon_rojo@hotmail.com"],  # A
                fail_silently=False,
            )
            return HttpResponse("Mensaje enviado con éxito.")
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact.html', {'form': form})