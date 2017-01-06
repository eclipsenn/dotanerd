# # -*- coding: utf-8 -*-

from django.contrib.auth import authenticate as auth_authenticate, login as auth_login
from django.contrib.auth.views import login as default_login, logout as default_logout
from django.contrib.auth.forms import UserCreationForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context_processors import csrf

from questions.models import Profile


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username', '')
            password = request.POST.get('password1', '')
            user = auth_authenticate(username=username, password=password)

            # create profile object
            profile = Profile()
            profile.user = user
            # profile.photo = json.loads(user_map.identity.data)['photo']
            profile.save()
            auth_login(request, user)
            return HttpResponseRedirect('/users/profile/')
    else:
        form = UserCreationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('register.html', token)


def profile(request):
    return render_to_response('profile.html')


def login(request):
    # TODO: is it needed?
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth_authenticate(username=username, password=password)

    return default_login(request, 'login.html')


def logout(request):
    return default_logout(request, template_name='home.html')