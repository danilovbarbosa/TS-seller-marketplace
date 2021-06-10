from django.urls import path
from .views import (
    seller_list,
    seller_create,
    seller_update,
    seller_delete,
    seller_detail,
)


urlpatterns = [
    path('', seller_list, name='seller_list'),
    path('create/', seller_create , name='seller_create'),
    path('<pk>/update/', seller_update, name='seller_update'),
    path('<pk>/delete/', seller_delete, name='seller_delete'),
    path('<pk>/delete/', seller_detail, name='seller_detail'),
]
