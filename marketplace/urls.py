from django.urls import path
from .views import (
    marketplace_list,
    marketplace_create,
    marketplace_update,
    marketplace_delete,
    marketplace_detail
)


urlpatterns = [
    path('', marketplace_list, name='marketplace_list'),
    path('create/', marketplace_create, name='marketplace_create'),
    path('<id>/update/', marketplace_update, name='marketplace_update'),
    path('<id>/delete/', marketplace_delete, name='marketplace_delete'),
    path('<id>/delete/', marketplace_detail, name='marketplace_detail'),
]
