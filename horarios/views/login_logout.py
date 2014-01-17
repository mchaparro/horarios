# -*- coding: utf-8 -*-
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext

# change to your app name!
from skeleton.models import *
##############################
from django.contrib.auth import authenticate, login, logout
from django.views.generic import UpdateView, CreateView
from django.contrib import messages

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