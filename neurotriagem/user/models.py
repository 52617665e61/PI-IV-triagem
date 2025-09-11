from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.models import Group


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, last_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('tipo', 'admin')

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, user_name, first_name, last_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, last_name, password, **other_fields):
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


class NewUser(AbstractBaseUser, PermissionsMixin):

    class TipoUsuario(models.TextChoices):
        NORMAL = 'normal', _('Usuário Normal')
        PSICOLOGO = 'psicologo', _('Psicólogo/Psiquiatra')
        ADMIN = 'admin', _('Administrador')

    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(_('Endereço de email'), unique=True)
    user_name = models.CharField(_('Usuário'), max_length=150, unique=True)
    first_name = models.CharField(_('Primeiro nome'), max_length=150)
    last_name = models.CharField(_('Sobrenome'), max_length=150)
    data_nascimento = models.DateField(_('Data de nascimento'))
    telefone = models.CharField(_('Telefone'), max_length=20, blank=True, null=True)

    # Campos específicos para psicólogos
    endereco_rua = models.CharField(max_length=255, blank=True, null=True)
    endereco_numero = models.CharField(max_length=10, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=15, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    registro_profissional = models.CharField(_('CRP ou CRM'), max_length=50, blank=True, null=True)

    data_registro = models.DateTimeField(_('Data de registro'), default=timezone.now)

    tipo = models.CharField(
        max_length=20,
        choices=TipoUsuario.choices,
        default=TipoUsuario.NORMAL
    )

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'data_nascimento']

    def __str__(self):
        return f"{self.user_name} ({self.tipo})"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Adiciona o usuário ao grupo apropriado, se ainda não estiver
        if self.tipo:
            grupo, created = Group.objects.get_or_create(name=self.tipo)
            self.groups.add(grupo)
