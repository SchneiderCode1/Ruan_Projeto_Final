from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from datetime import timezone
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    def __str__(self):
        return self.user.username

class Cadastro(models.Model):
    nome = models.CharField(max_length=150, null=False, blank=False, unique=True)
    username = models.CharField(max_length=30, null=False, blank=False, unique=True)
    email = models.EmailField(max_length=50, null=False, blank=False, unique=True, primary_key=True)
    senha = models.CharField(max_length=30, null=False, blank=False)
    senha_confirma = models.CharField(max_length=30, null=False, blank=False)
    def __str__(self):
        return f'{self.email} : {self.username}'