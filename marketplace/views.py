from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from django.urls import reverse

from marketplace.models import Marketplace 

class MarketplaceListView(ListView):
    model = Marketplace


class MarketplaceCreateView(CreateView):
    model = Marketplace
    fields = ['name', 'document', 'phone_number', 'email', 'sellers']
    
    
    def get_success_url(self):
        return reverse('list')
    

class MarketplaceUpdateView(UpdateView):
    model = Marketplace
    fields = ['name', 'document', 'phone_number', 'email']
    
    
    def get_success_url(self):
        return reverse('list')
    

class MarketplaceDeleteView(DeleteView):
    # specify the model you want to use
    model = Marketplace
     
    def get_success_url(self):
        return reverse('list')


class MarketplaceDetailView(DetailView):
    
    model = Marketplace