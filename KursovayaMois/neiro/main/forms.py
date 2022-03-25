from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.core.exceptions import ValidationError

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        # fields = "__all__"
        fields = ('username', 'fio', 'gender', 'birth_date', 'image', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = "__all__"
        fields = ('username', 'fio', 'gender', 'birth_date', 'image', 'email')

        def clean(self):
            cleaned_data = super().clean()
            if CustomUser.objects.filter(email=cleaned_data.get('email')).exists():
                raise ValidationError('Bad email, bro')


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Enter old password'}))
    new_password1 = forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Enter new password'}))
    new_password2 = forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Confirm new password'}))

    class Meta:
        model = CustomUser
        fields = ["old_password", "new_password1", "new_password2"]
