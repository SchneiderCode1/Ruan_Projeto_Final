from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import CadastroForm
from .forms import LoginForm
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.core.mail import send_mail
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from datetime import timezone
import json
from django.utils.timezone import make_aware
from django.utils import timezone
from django.utils.encoding import force_str
from django.conf import settings
from datetime import datetime

# Create your views here.
def cadastro(request):
    context = {}
    form = CadastroForm()
    context["form"] = form
    return render(request, "cadastro.html", context)

def login(request):
    if not request.user.is_authenticated:
        context = {}
        form = LoginForm()
        context["form"] = form
    return render(request, "login.html")
    