from django.urls import path
# from .views import index
from .views import (
    SellerListView,
    SellerCreateView
)


urlpatterns = [
    path('', SellerListView.as_view(), name='list'),
    path('create/', SellerCreateView.as_view(), name='create'),

]
