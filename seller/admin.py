from django.contrib import admin
from .models import Address, Contact, Seller
# Register your models here.


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    pass


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass