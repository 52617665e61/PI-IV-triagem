from django.urls import path
from .views import register_view

urlpatterns = [
    path('registro/', register_view, name='registro'),
]
