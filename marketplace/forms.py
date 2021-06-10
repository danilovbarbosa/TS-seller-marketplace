from django.forms import ModelForm

from marketplace.models import Marketplace


class MarketplaceForm(ModelForm):

    class Meta:
        model = Marketplace
        fields = ['name', 'document', 'email', 'sellers']