from django.shortcuts import render

from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from django.urls import reverse

from seller.models import Seller

class SellerListView(ListView):
    model = Seller


class SellerCreateView(CreateView):
    template_name = 'seller/new_seller.html'
    model = Seller
    fields = ['name', 'document', 'phone_number', 'email']
    
    
    def get_success_url(self):
        return reverse('list')