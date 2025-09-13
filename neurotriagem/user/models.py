from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.models import Group


# Gerenciador de contas personalizado
class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, user_name, first_name, last_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        return self.create_user(email, user_name, first_name, last_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, last_name, password=None, **other_fields):
        if not email:
            raise ValueError(_('Você deve fornecer um endereço de e-mail'))

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            user_name=user_name,
            first_name=first_name,
            last_name=last_name,
            **other_fields
        )
        user.set_password(password)
        user.save()
        return user


# Modelo base de usuário (usado para autenticação)
class NewUser(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(_('Endereço de email'), unique=True)
    user_name = models.CharField(_('Usuário'), max_length=150, unique=True)
    first_name = models.CharField(_('Primeiro nome'), max_length=150)
    last_name = models.CharField(_('Sobrenome'), max_length=150)
    data_registro = models.DateTimeField(_('Data de registro'), default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.user_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # (Opcional) Adicionar a um grupo padrão com base no tipo real
        real_instance = getattr(self, 'get_real_instance', lambda: None)()
        if real_instance:
            group_name = type(real_instance).__name__.replace('User', '').lower()
            grupo, _ = Group.objects.get_or_create(name=group_name)
            self.groups.add(grupo)

    def get_real_instance(self):
        """Retorna a instância real (subclasse)"""
        for subclass in (NormalUser, PsicologoUser, AdminUser):
            try:
                return subclass.objects.get(pk=self.pk)
            except subclass.DoesNotExist:
                continue
        return self

class NormalUser(NewUser):
    data_nascimento = models.DateField(_('Data de nascimento'))
    telefone = models.CharField(_('Telefone'), max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = "Usuário Normal"
        verbose_name_plural = "Usuários Normais"


class PsicologoUser(NewUser):
    data_nascimento = models.DateField(_('Data de nascimento'))
    telefone = models.CharField(_('Telefone'), max_length=20, blank=True, null=True)
    registro_profissional = models.CharField(_('CRP ou CRM'), max_length=50)
    endereco_rua = models.CharField(max_length=255, blank=True, null=True)
    endereco_numero = models.CharField(max_length=10, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=15, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = "Psicólogo"
        verbose_name_plural = "Psicólogos"


class AdminUser(NewUser):
    cargo = models.CharField(_('Cargo'), max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"
