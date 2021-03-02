from django.shortcuts import render
from django.views.generic import CreateView, View
from django.views.generic.edit import FormView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .forms import UserRegisterForm, LoginForm, UpdatePasswordForm
from .models import User


class UserRegisterView(FormView):
    template_name = 'users/user_register.html'
    form_class = UserRegisterForm
    success_url = '.'

    def form_valid(self, form):
        User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'],
                                 form.cleaned_data['password1'], nombre=form.cleaned_data[
                                     'nombre'], apellidos=form.cleaned_data['apellidos'],
                                 genero=form.cleaned_data['genero'])
        return super(UserRegisterView, self).form_valid(form)


class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:home_panel')

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


class LogOut(View):
    def get(self, request, *args, **kwords):
        logout(request)
        return HttpResponseRedirect(reverse('users_app:login_user'))


class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = "users/update_password.html"
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('users_app:login_user')
    login_url = reverse_lazy('users_app:login_user')

    def form_valid(self, form):
        usuario = self.request.user
        user = authenticate(
            username=usuario.username, password=form.cleaned_data['password1'])
        if user:
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()

        logout(self.request)
        return super(UpdatePasswordView, self).form_valid(form)
