from django.urls import path
from analytics import views

app_name = 'analytics'  

urlpatterns = [
    path('modelo/', views.dashboard_modelo, name='dashboard_modelo'),
    path('geral/', views.dashboard_geral, name='dashboard_geral'),
    path('individual/<int:teste_id>/', views.dashboard_individual, name='dashboard_individual'),
]