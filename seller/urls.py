from django.urls import path
from .views import (
    SellerListView,
    SellerCreateView,
    SellerUpdateView,
    SellerDeleteView,
    SellerDetailView
)


urlpatterns = [
    path('', SellerListView.as_view(), name='seller_list'),
    path('create/', SellerCreateView.as_view(), name='seller_create'),
    path('<pk>/update/', SellerUpdateView.as_view(), name='seller_update'),
    path('<pk>/delete/', SellerDeleteView.as_view(), name='seller_delete'),
    path('<pk>/delete/', SellerDetailView.as_view(), name='seller_detail'),
]
