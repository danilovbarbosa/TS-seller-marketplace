from django.contrib import admin
from .models import Marketplace
# Register your models here.


@admin.register(Marketplace)
class MarketplaceAdmin(admin.ModelAdmin):
    pass
