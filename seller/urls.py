from django.urls import path
from .views import (
    SellerListView,
    SellerCreateView,
    SellerUpdateView,
    SellerDeleteView,
    SellerDetailView
)


urlpatterns = [
    path('', SellerListView.as_view(), name='list'),
    path('create/', SellerCreateView.as_view(), name='create'),
    path('<pk>/update/', SellerUpdateView.as_view(), name='update'),
    path('<pk>/delete/', SellerDeleteView.as_view(), name='delete'),
    path('<pk>/delete/', SellerDetailView.as_view(), name='detail'),
]
