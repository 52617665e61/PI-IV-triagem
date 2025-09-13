from django.urls import path
from . import views

app_name = 'analytics'

urlpatterns = [
    path('', views.dashboard_view, name='visao_geral'),
    path('paciente/<int:paciente_id>/', views.paciente_detail_view, name='paciente_detail'),
]