from django.urls import path
from triagem import views

app_name = 'Triagem'

urlpatterns = [
    path('teste/<slug:teste_nome>/', views.triagem_view, name='triagem'),
]