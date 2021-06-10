from django.urls import path
from .views import (
    base_home,
)


urlpatterns = [
    path('', base_home, name='base_home'),
]