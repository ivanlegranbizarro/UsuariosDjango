from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
# create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (('H', 'Hombre cisgénero'),
                      ('M', 'Mujer cisgénero'), ('O', 'Persona no cisgénero'),)
    username = models.CharField('Usuario', max_length=50, unique=True)
    email = models.EmailField()
    nombre = models.CharField('Nombre', max_length=20, blank=True)
    apellidos = models.CharField('Apellidos', max_length=40, blank=True)
    genero = models.CharField('Género', max_length=1,
                              choices=GENDER_CHOICES, blank=True)
    cod_registro = models.CharField(
        'Código de confirmación', max_length=6, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

    # def get_short_name(self):
    #     return self.username

    # def get_full_name(self):
    #     return self.nombre + ' | ' + self.apellidos

    def __str__(self):
        return self.username
