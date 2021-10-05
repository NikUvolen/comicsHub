from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='User name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password input', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    def is_valid(self):
        result = super().is_valid()
        for x in self.fields:
            attrs = self.fields[x].widget.attrs
            if ("__all__" in self.errors) or (x in self.errors):
                error_css_class = 'is-invalid'
            else:
                error_css_class = 'is-valid'
            attrs.update({'class': attrs.get('class', '') + ' ' + error_css_class})
        return result

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='User name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password input', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
