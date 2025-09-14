from django.contrib import admin
from .models import NormalUser, PsicologoUser, AdminUser

# Register your models here.

admin.site.register(NormalUser)
admin.site.register(PsicologoUser)
admin.site.register(AdminUser)