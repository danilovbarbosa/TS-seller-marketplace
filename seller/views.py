from django.shortcuts import (get_object_or_404,
                              render,
                              redirect,
                              HttpResponseRedirect)

from seller.forms import SellerForm, AddressForm, ContactForm

from seller.models import Address, Contact, Seller


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


def seller_update(request, id):
 
    seller_obj = get_object_or_404(Seller, id = id)
    seller_form = SellerForm(request.POST or None, instance = seller_obj)
    
    address_obj = Address.objects.get(seller=id)
    address_form = AddressForm(request.POST or None, instance = address_obj)

    contact_obj = Contact.objects.get(seller=id)
    contact_form = ContactForm(request.POST or None, instance = contact_obj)
    
    if seller_form.is_valid() and address_form.is_valid() and contact_form.is_valid():
        seller_form.save()
        address_form.save()
        contact_form.save()
        
        return redirect('seller_list')
 
    context = {
        'seller_form' : seller_form,
        'address_form' : address_form,
        'contact_form' : contact_form,
    }    
    
    return render(request, 'seller/seller_form.html', context=context)

def seller_delete(request, id):
    context = {}

    obj = get_object_or_404(Seller, id = id)
    
    if request.method == "GET":
        obj.delete()

        return redirect('seller_list')
    
    return render(request, 'seller/seller_list.html', context=context)


def seller_detail(request):
    seller_list = Seller.objects.all()
    context = {
        'seller_list' : seller_list,
    }
    
    return render(request, 'seller/seller_list.html', context=context)
