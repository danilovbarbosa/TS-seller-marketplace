from django.urls import path
from .views import (
    MarketplaceListView,
    MarketplaceCreateView,
    MarketplaceUpdateView,
    MarketplaceDeleteView,
    MarketplaceDetailView
)


urlpatterns = [
    path('', MarketplaceListView.as_view(), name='marketplace_list'),
    path('create/', MarketplaceCreateView.as_view(), name='marketplace_create'),
    path('<pk>/update/', MarketplaceUpdateView.as_view(), name='marketplace_update'),
    path('<pk>/delete/', MarketplaceDeleteView.as_view(), name='marketplace_delete'),
    path('<pk>/delete/', MarketplaceDetailView.as_view(), name='marketplace_detail'),
]
