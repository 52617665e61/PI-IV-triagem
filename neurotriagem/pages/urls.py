from django.urls import path
from pages import views

app_name = 'pages'  

urlpatterns = [
    path('', views.index, name='index'),
    path('serviços/', views.lista_de_servicos, name='servicos'),
    path('quem_somos', views.quem_somos, name='quem_somos'),
]