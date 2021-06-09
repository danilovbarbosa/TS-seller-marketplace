from django.urls import path
from .views import (
    SellerListView,
    SellerCreateView,
    SellerDeleteView
)


urlpatterns = [
    path('', SellerListView.as_view(), name='list'),
    path('create/', SellerCreateView.as_view(), name='create'),
    # <pk> is identification for id field,
    # slug can also be used
    path('<pk>/delete/', SellerDeleteView.as_view(), name='delete'),
]
