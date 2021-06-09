from django.shortcuts import render
from django.urls.base import reverse_lazy

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from django.urls import reverse

from seller.models import Seller

class SellerListView(ListView):
    model = Seller


class SellerCreateView(CreateView):
    # template_name = 'seller/seller_form.html'
    model = Seller
    fields = ['name', 'document', 'phone_number', 'email']
    
    
    def get_success_url(self):
        return reverse('list')
    

class SellerUpdateView(UpdateView):
    model = Seller
    fields = ['name', 'document', 'phone_number', 'email']
    
    
    def get_success_url(self):
        return reverse('list')
    

class SellerDeleteView(DeleteView):
    # specify the model you want to use
    model = Seller
     
    def get_success_url(self):
        return reverse('list')


class SellerDetailView(DetailView):
    
    model = Seller

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['seller_list'] = Seller.objects.all()
        return context