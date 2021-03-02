from django import forms
from .models import User
from django.contrib.auth import authenticate


class UserRegisterForm(forms.ModelForm):
    """Form definition for UserRegister."""
    password1 = forms.CharField(
        label='Contraseña', required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Ingresa tu contraseña', 'class': 'form-control', 'autocomplete': 'off'}))

    password2 = forms.CharField(
        label='Contraseña', required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Repite tu contraseña', 'class': 'form-control', 'autocomplete': 'off'}))

    class Meta:
        """Meta definition for UserRegisterform."""
        model = User
        fields = ('username', 'email', 'nombre', 'apellidos', 'genero',)
        # widgets = {
        #     'username': forms.TextInput(attrs={'autocomplete': 'penis'}),
        #     'email': forms.EmailInput(attrs={'autocomplete':'penis'}),
        #     'password1': forms.PasswordInput(attrs={'autocomplete': 'penis'})
        # }

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password1', 'Las contraseñas deben coincidir')
        elif len(self.cleaned_data['password1']) < 5:
            self.add_error(
                'password1', 'La contraseña debe tener al menos cinco dígitos')


class LoginForm(forms.Form):
    username = forms.CharField(label='username', required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Ingresa tu usuario', 'class': 'form-control'}))
    password = forms.CharField(label='Contraseña', required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Ingresa tu contraseña', 'class': 'form-control', 'autocomplete': 'off'}))

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username, password=password):
            raise forms.ValidationError(
                'Los datos no pertenecen a un usuario registrado')
        return self.cleaned_data


class UpdatePasswordForm(forms.Form):
    password1 = forms.CharField(label='Contraseña antigua', required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Ingrese su antigua contraseña', 'class': 'form-control'}))
    password2 = forms.CharField(label='Nueva contraseña', required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese su nueva contraseña',
                                                                  'class': 'form-control'}))
