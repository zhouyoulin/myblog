from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from . import forms

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request,user)
                return HttpResponseRedirect("/blog/blog_title")
            else:
                return HttpResponse('your account or password error')
        else:
            return HttpResponse('invalid login')
    if request.method == 'GET':
        return render(request, 'account/login.html', {'form': forms.LoginForm})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/blog/blog_title")