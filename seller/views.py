from seller.models import Seller
from django.shortcuts import render

from django.views.generic.edit import CreateView
from django.views.generic.list import ListView


class SellerListView(ListView):
    model = Seller
    # queryset = Seller.objects.all()
    # context_object_name = 'seller_list'


class SellerCreateView(CreateView):
    template_name = 'seller/new_seller.html'
    model = Seller
    fields = ['name', 'document', 'phone_number', 'email']
    
    # def form_valid(self):
    #     return super().form_valid(form)



# def index(request):
#     list_sellers = Seller.objects.all()
    
#     context = {
#         'list_sellers' : list_sellers
#     }
    
#     return render(request, 'seller/seller_list.html', context=context)


# def create(request):
#     context = {}
#     return render(request, 'seller/new_seller.html', context=context)