from django.forms import DateInput, ModelForm
from django import forms 
from .models import *

class CadastroForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CadastroForm, self).__init__(*args, **kwargs)
        
        self.fields['nome'].widget.attrs = {'class' : '', 'autocomplete' : '', 'name': '', 'type' : '', 'placeholder' : 'Digite o seu nome completo', 'oninput' : ''}
        self.fields['username'].widget.attrs = {'class' : '', 'autocomplete' : '', 'name': '', 'type' : '', 'placeholder' : 'Escolha um nome para o seu usuario', 'oninput' : ''}
        self.fields['email'].widget.attrs = {'class' : '', 'autocomplete' : '', 'name': '', 'type' : '', 'placeholder' : 'Digite o seu email', 'oninput' : ''}
        self.fields['senha'].widget.attrs = {'class' : '', 'autocomplete' : '', 'name': '', 'type' : '', 'placeholder' : 'Digite a sua senha', 'oninput' : ''}
        self.fields['senha_confirma'].widget.attrs = {'class' : '', 'autocomplete' : '', 'name': '', 'type' : '', 'placeholder' : 'Repita a sua senha', 'oninput' : ''}
    
    class Meta:
        model = Cadastro
        fields = ['nome', 'username', 'email', 'senha', 'senha_confirma']

class LoginForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        
        self.fields['email'].widget.attrs = {'class' : '', 'autocomplete' : '', 'name': 'Email', 'type' : 'email', 'placeholder' : 'Digite o seu email', 'oninput' : ''}
        self.fields['senha'].widget = forms.PasswordInput()
        self.fields['senha'].widget.attrs = {'class' : '', 'autocomplete' : '', 'name': 'Senha', 'type' : 'password', 'placeholder' : 'Digite a sua senha', 'oninput' : ''}
        
    class Meta:
        model = Cadastro
        fields = ['email', 'senha']