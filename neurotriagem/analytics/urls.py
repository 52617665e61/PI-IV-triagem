from django.urls import path
from . import views

app_name = 'analytics'

urlpatterns = [
    path('', views.dashboard_view, name='visao_geral'),
    path('lista_de_pacientes', views.pacients_list, name='pacients_list'),
    path('paciente/<int:id>/', views.paciente_detail_view, name='pacient_detail'),
    path('teste/<int:id>/', views.triagem_detail_view, name='triagem_detail'),
]

