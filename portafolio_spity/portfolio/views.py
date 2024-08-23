from django.shortcuts import get_object_or_404, render
from django.views.decorators.clickjacking import xframe_options_sameorigin

from .models import PortfolioDesc, PortfolioItem


# Create your views here.
@xframe_options_sameorigin
def portfolio(request):
    items = PortfolioItem.objects.all().order_by('-project_date')
    portfolio_desc = PortfolioDesc.objects.last()
    return render(
        request,
        "portfolio/portfolio.html",
        {"items": items, "portfolio_desc": portfolio_desc},
    )


def portfolio_details(request, pk):
    item = get_object_or_404(PortfolioItem, pk=pk)
    return render(request, "portfolio/portfolio-details.html", {"item": item})
