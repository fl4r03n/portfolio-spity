from django.shortcuts import render

from .models import Education, Experience, ResumeDesc


def resume(request):
    educations = Education.objects.all().order_by("-start_year")
    experiences = Experience.objects.all().order_by("-start_year")
    resume_desc = ResumeDesc.objects.last()

    for exp in experiences:
        exp.responsibilities_list = exp.responsibilities.split(",")

    context = {
        "educations": educations,
        "experiences": experiences,
        "resume_desc": resume_desc,
    }

    return render(request, "resume/resume.html", context)
