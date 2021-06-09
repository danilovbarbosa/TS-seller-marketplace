from seller.models import Seller
from django.shortcuts import render

from django.views.generic.edit import CreateView
from django.views.generic.list import ListView


class SellerListView(ListView):
    model = Seller


class SellerCreateView(CreateView):
    template_name = 'seller/new_seller.html'
    model = Seller
    fields = ['name', 'document', 'phone_number', 'email']
    