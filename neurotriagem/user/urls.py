from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro_escolha_view, name='registro_escolha'),
    path('registro/<str:tipo>/', views.register_view, name='registro'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
]
