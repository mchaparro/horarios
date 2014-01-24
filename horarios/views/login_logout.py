# -*- coding: utf-8 -*-
from django.http import *
from django.shortcuts import render_to_response,redirect,render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
# change to your app name!
from horarios.models import *
##############################
from django.contrib.auth import authenticate, login, logout
from django.views.generic import UpdateView, CreateView
from django.contrib import messages
from horarios.views.dias_semana import *

def login_user(request):
    try:
        next = request.GET['next']
    except:
        next = '/'
        
    logout(request)
    email = ''
    password = ''
    if request.POST:
        usuario = request.POST['usuario']
        password = request.POST['password']
        user = authenticate(usuario=usuario, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
            return HttpResponseRedirect(next)
        
    return render_to_response('login.html', context_instance=RequestContext(request))

def logout_user(request):
  logout(request)
  return redirect(login_user)

@login_required 
def home(request):
    return render(request, 'home.html', {'semana_actual': semana_actual()})

@login_required 
def administrador(request):
    return render(request, 'admin.html', {'semana_actual': semana_actual()})