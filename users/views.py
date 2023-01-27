from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth.models import Group
from . import forms


class SignUpView(CreateView):
    form_class = forms.CustomUserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    model = CustomUser

    def form_valid(self, form):

        response = super().form_valid(form)
        group = Group.objects.get(name="Criador")
        user = form.instance
        user.groups.add(group.id)
        user.save()
        messages.success(self.request, "Usuário cadastrado com sucesso!")
        return response
