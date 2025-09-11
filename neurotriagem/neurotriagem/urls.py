from django.contrib import admin
from django.urls import path, include
from triagem import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  
    path('triagem/', views.triagem_view, name='triagem_tdh'),  # movemos a view para outra rota
    path('dashboards/', include('analytics.urls')),
]
