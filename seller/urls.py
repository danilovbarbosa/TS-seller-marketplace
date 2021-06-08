from django.urls import path
# from .views import index
from .views import (
    SellerList,
    SellerCreateView
)


urlpatterns = [
    # path('', index, name='index'),
    # path('new_seller', views.create, name='create'),
    path('', SellerList.as_view(), name='list'),
    path('create/', SellerCreateView.as_view(), name='create'),

]
