
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import RegistrationForm, ChangeUserFormData
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from posts.models import Post
# Create your views here.


def register(request):
    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            messages.success(request, 'Account Created Successfully')
            register_form.save()
    else:
        register_form = RegistrationForm()
    return render(request, 'author/author.html', {'forms': register_form, 'type': 'Register'})


# def user_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['username']
#             user_pass = form.cleaned_data['password']
#             user = authenticate(username=name, password=user_pass)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, 'Account Login Successfully')
#                 return redirect('home')
#             else:
#                 messages.warning(
#                     request, 'You are not authenticate, please register')
#                 return redirect('register')
#     else:
#         form = AuthenticationForm()
#         return render(request, 'author/author.html', {'form': form, 'type': 'Login'})


class UserLoginView(LoginView):
    template_name = 'author/author.html'

    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'User Login Successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, 'Login Information is Incorrect')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context


@login_required
def profile(request):
    data = Post.objects.filter(author=request.user)
    return render(request, 'author/profile.html', {'data': data})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = ChangeUserFormData(request.POST, instance=request.user)
        if profile_form.is_valid():
            messages.success(request, 'Profile Updated Successfully')
            profile_form.save()
            return redirect('profile')
    else:
        profile_form = ChangeUserFormData(instance=request.user)
    return render(request, 'author/update_profile.html', {'forms': profile_form})


@login_required
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'author/passchange.html', {'forms': form, })


def user_logout(request):
    logout(request)
    return redirect('user_login')
