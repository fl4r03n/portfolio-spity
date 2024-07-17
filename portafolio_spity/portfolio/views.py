from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.decorators.clickjacking import xframe_options_deny
from django.views.decorators.clickjacking import xframe_options_sameorigin
from .models import PortfolioItem, PortfolioDesc
# Create your views here.
@xframe_options_sameorigin
def portfolio(request):
    items = PortfolioItem.objects.all()
    portfolio_desc = PortfolioDesc.objects.last()
    return render(request, 'portfolio/portfolio.html', {'items': items,'portfolio_desc': portfolio_desc})

def portfolio_details(request, pk):
    item = get_object_or_404(PortfolioItem, pk=pk)
    return render(request, 'portfolio/portfolio-details.html', {'item': item})