from django.shortcuts import render

from .models import Service, ServicesDesc

BRAND_ICONS = [
    "500px",
    "amazon",
    "android",
    "apple",
    "behance",
    "bitcoin",
    "blogger",
    "bootstrap",
    "chrome",
    "codepen",
    "css3",
    "discord",
    "dribbble",
    "dropbox",
    "facebook",
    "figma",
    "firefox",
    "flickr",
    "github",
    "google",
    "html5",
    "instagram",
    "java",
    "javascript",
    "joomla",
    "kickstarter",
    "linkedin",
    "magento",
    "medium",
    "microsoft",
    "nodejs",
    "pinterest",
    "python",
    "react",
    "reddit",
    "sass",
    "shopify",
    "skype",
    "slack",
    "snapchat",
    "soundcloud",
    "spotify",
    "squarespace",
    "stack-overflow",
    "steam",
    "telegram",
    "tiktok",
    "tumblr",
    "twitch",
    "twitter",
    "vuejs",
    "whatsapp",
    "wordpress",
    "yahoo",
    "youtube",
]


def services(request):
    services_desc = ServicesDesc.objects.last()
    services = Service.objects.all()
    brand_icons = BRAND_ICONS
    return render(
        request,
        "services/services.html",
        {
            "services_desc": services_desc,
            "services": services,
            "brand_icons": brand_icons,
        },
    )
