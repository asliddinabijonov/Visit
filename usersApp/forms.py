from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import TurUser

class TurUserRegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label="Parol",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parol'})
    )
    password2 = forms.CharField(
        label="Parolni tasdiqlang",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parolni tasdiqlang'})
    )

    class Meta:
        model = TurUser
        fields = [
            'username', 'email', 'user_type', 'phone',
            'country', 'city', 'avatar', 'description'
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Foydalanuvchi nomi'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email manzili'}),
            'user_type': forms.Select(attrs={'class': 'form-select'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon raqam'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Davlat'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Shahar'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Qo‘shimcha ma’lumot', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Parol maydonlarini styling bilan bir xil qilish uchun
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
