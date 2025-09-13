from django.urls import path
from analytics1 import views

app_name = 'analytics1'  

urlpatterns = [
    path('modelo/', views.dashboard_modelo, name='dashboard_modelo'),
    path('geral/', views.dashboard_geral, name='dashboard_geral'),
    path('individual/<int:teste_id>/', views.dashboard_individual, name='dashboard_individual'),
]