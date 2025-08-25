from django.contrib import admin
from django.urls import path
from triagem import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.triagem_view, name='triagem_tdh'),
]
