from django import forms
from .models import Usuario

class LoginForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'input-field', 
                'placeholder': 'Usuario',
                'autocomplete': 'off'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'input-field', 
                'placeholder': 'Contraseña',
                'autocomplete': 'off'
            }),
        }