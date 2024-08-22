from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# Create your views here.


def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, "User Created Successfully")
                form.save()
            else:
                print(form.errors)
        else:
            form = forms.RegisterForm()
        return render(request, 'signup/signup.html', {'forms': form})
    else:
        return redirect('user_profile')


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                user_pass = form.cleaned_data['password']
                # is user is available in database
                user = authenticate(username=name, password=user_pass)
                if user is not None:
                    login(request, user)
                    print(user)
                    return redirect('/user-signup/user_profile/')
        else:
            form = AuthenticationForm()
            return render(request, 'signup/login.html', {'forms': form})
    else:
        return redirect('user_profile')
    return render(request, 'signup/login.html', {'forms': form})


def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.ChangeData(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request, "User Updated Successfully")
                form.save()
            else:
                print(form.errors)
        else:
            form = forms.ChangeData(instance=request.user)
        return render(request, 'signup/userprofile.html', {'forms': form})
    else:
        return redirect('sign_up')
    # if request.user.is_authenticated:
    #     return render(request, 'signup/userprofile.html', {'users': request.user})
    # else:
    #     return redirect('login')


def user_logout(request):
    logout(request)
    return redirect('login')


def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('user_profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'signup/password.html', {'form': form})
    else:
        return redirect('login')


def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('user_profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, 'signup/password_two.html', {'form': form})
    else:
        return redirect('login')
