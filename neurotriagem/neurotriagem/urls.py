from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),  
    path('triagem/', include('triagem.urls')), 
    path('dashboards/', include('analytics.urls')),
    path('user/', include('user.urls')),
]
