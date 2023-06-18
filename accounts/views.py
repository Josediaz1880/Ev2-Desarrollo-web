from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import CustomUser
from .forms import *
from django.contrib.auth.views import LoginView, LogoutView



class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = '/login/'
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


class CustomLogoutView(LogoutView):
    template_name = 'registration/login.html'


""" ----------------------------------------------------------------- """


def crearUsuario(request):
    form = CustomUserCreationForm()
    if (request.method == 'POST'):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            usu = form.cleaned_data
            print(usu)
            print("datos validos")
            form.save()
            form = ''
            return redirect("/usuarios")
    data = {'form': form, 'titulo': 'Ingresar nuevo usuario'}
    return render(request, 'gestion/crearUsuario.html', data)


def editarUsuario(request, id):
    usuario = CustomUser.objects.get(id=id)
    data = {
        'form': CustomUserCreationForm(instance=usuario),
        'titulo': 'Editar usuario'
    }
    if (request.method == 'POST'):
        form = CustomUserCreationForm(request.POST, instance=usuario)
        if (form.is_valid()):
            form.save()
            return redirect("/usuarios")
        else:
            data['form'] = form
    return render(request, 'gestion/crearUsuario.html', data)



""" ----------------------------------------------------------------- """
