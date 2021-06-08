from django.contrib import admin
from .models import Address, Seller
# Register your models here.


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    pass


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass