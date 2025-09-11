from django.urls import path
from .views import register_view,CustomLoginView, CustomLogoutView

urlpatterns = [
    path('registro/', register_view, name='registro'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
