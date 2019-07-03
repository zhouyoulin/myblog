from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from . import forms, models

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
        login_form = forms.LoginForm()
        return render(request, 'account/login.html', {'form': login_form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/blog/blog_title")

def user_register(request):
    if request.method == 'POST':
        user_form = forms.RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return user_login(request)
        else:
            return HttpResponse(user_form)
    else:
        user_form = forms.RegisterForm()
        return render(request,'account/register.html', {'form': user_form})

def user_info(request, user_id):
    user = get_object_or_404(User, id=user_id)
    # User.objects.get()
    userInfos = models.UserInfo.objects.all()
    userInfo = None
    for userinfo in userInfos:
        if userinfo.user.id == int(user_id):
            userInfo = userinfo
    if request.method == 'POST':
        userInfo_form = forms.UserInfoForm(request.POST)
        if userInfo_form.is_valid():
            cd = userInfo_form.cleaned_data
            print(cd)
            if userInfo:
                userInfo.birth = cd['birth']
                userInfo.phone = cd['phone']
                userInfo.user = user
                userInfo.save()
            else:
                userInfo = models.UserInfo.objects.create(user=user,birth=cd['birth'],phone=cd['phone'])
                userInfo.save()
            return HttpResponseRedirect("/account/userInfo/"+user_id)
        else:
            return HttpResponse('form is invalid')
    else:
        return render(request, 'account/user_info.html',{'userInfo':userInfo})