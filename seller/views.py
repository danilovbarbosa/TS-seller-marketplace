from django.shortcuts import render

from seller.forms import SellerForm

from seller.models import Seller


def seller_list(request):
    seller_list = Seller.objects.all()
    context = {
        'seller_list' : seller_list,
    }
    
    return render(request, 'seller/seller_list.html', context=context)


def seller_create(request):
    seller_list = Seller.objects.all()
    context = {
        'seller_list' : seller_list,
    }
    
    return render(request, 'seller/seller_list.html', context=context)


def seller_update(request):
    seller_list = Seller.objects.all()
    context = {
        'seller_list' : seller_list,
    }
    
    return render(request, 'seller/seller_list.html', context=context)


def seller_delete(request):
    seller_list = Seller.objects.all()
    context = {
        'seller_list' : seller_list,
    }
    
    return render(request, 'seller/seller_list.html', context=context)


def seller_detail(request):
    seller_list = Seller.objects.all()
    context = {
        'seller_list' : seller_list,
    }
    
    return render(request, 'seller/seller_list.html', context=context)
