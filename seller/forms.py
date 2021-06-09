from django.forms import ModelForm

from seller.models import Seller, Address, Contact


class SellerForm(ModelForm):
    
    class Meta:
        model = Seller
        fields = ['name', 'document', 'phone_number', 'email']

class AddressForm(ModelForm):
    
    class Meta:
        model = Address
        fields = ['number', 'street', 'district', 'city', 'state', 'zip_code', 'seller']
        
class ContactForm(ModelForm):
    
    class Meta:
        model = Contact
        fields = ['number', 'seller']
