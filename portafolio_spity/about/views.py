from django.shortcuts import render

from .models import (
    About,
    Fact,
    FactDesc,
    Skill,
    SkillDesc,
    Testimonial,
    TestimonialDesc,
)


def about(request):
    about_context = About.objects.last()

    skills_desc = SkillDesc.objects.last()
    skills = Skill.objects.all()
    half = (len(skills) + 1) // 2
    left_skills = skills[:half]
    right_skills = skills[half:]

    facts_desc = FactDesc.objects.last()
    facts = Fact.objects.all()

    testimonials_desc = TestimonialDesc.objects.last()
    testimonials = Testimonial.objects.all()

    return render(
        request,
        "about/about.html",
        {
            "about_context": about_context,
            "skills_desc": skills_desc,
            "left_skills": left_skills,
            "right_skills": right_skills,
            "facts_desc": facts_desc,
            "facts": facts,
            "testimonials_desc": testimonials_desc,
            "testimonials": testimonials,
        },
    )
