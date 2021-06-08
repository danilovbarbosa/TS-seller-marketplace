from seller.models import Seller
from django.shortcuts import render

# Create your views here.
def index(request):
    list_sellers = Seller.objects.all()
    
    context = {
        'list_sellers' : list_sellers
    }
    
    return render(request, 'seller/index.html', context=context)


def create(request):
    context = {}
    return render(request, 'seller/new_seller.html', context=context)