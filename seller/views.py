from django.shortcuts import redirect, render

from seller.forms import SellerForm, AddressForm, ContactForm

from seller.models import Seller


def seller_list(request):
    seller_list = Seller.objects.all()
    context = {
        'seller_list' : seller_list,
    }
    
    return render(request, 'seller/seller_list.html', context=context)


def seller_create(request):
    seller_form = SellerForm(request.POST or None)
    address_form = AddressForm(request.POST or None)
    contact_form = ContactForm(request.POST or None)

    if seller_form.is_valid() :
        new_seller = seller_form.save()
        
        new_address = address_form.save()
        new_address.seller = new_seller
        new_address.save()
        
        new_contact = contact_form.save()
        new_contact.seller = new_seller
        new_contact.save()

        return redirect('seller_list')
        
    context = {
        'seller_form' : seller_form,
        'address_form' : address_form,
        'contact_form' : contact_form,
    }
    
    return render(request, 'seller/seller_form.html', context=context)


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
