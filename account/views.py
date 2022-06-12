from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db.models import  F
from .forms import *
from post.models import Link
from .models import UserData

def Login(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))


    form= LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['parol'])
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                messages.error(request, 'Daxil etdiyiniz şifrə və ya telefon nömrəsi yanlışdır. Zəhmət olmasa bir daha sınayın.')

    else:
        form = LoginForm()
    contex = {
        'form': form,
    }


    return render(request, 'login.html', contex)

import random
import string
def Register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))

    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password1')
            user.set_password(password)

            
            while True:
                letters = string.digits
                newslug = ''.join(random.choice(letters) for i in range(8))
                userlist = User.objects.all().values_list('last_name', flat=True)
                if newslug not in userlist:
                    user.last_name = newslug    
                    break



            user.save()
            UserData.objects.create(user=user, clicklink=0, coins=0)
            new_user = authenticate(username=user.username, password=password)

            login(request, new_user)

            return HttpResponseRedirect(reverse('home'))

    else:
        form = RegisterForm()

    contex = {
        'form': form,
    }

    return render(request, 'register.html', contex)


def Profile(request, username):
    user = User.objects.get(username=username)

    user_links = Link.objects.filter(user=user)



    contex = {
        'user': user,
        'links': user_links,
    }

    return render(request, 'profile.html', contex)


def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


# Create your views here.
