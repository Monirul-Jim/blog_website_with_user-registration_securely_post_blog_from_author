from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from . models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def add_post(request):
    if request.method == 'POST':
        post = forms.PostForm(request.POST)
        if post.is_valid():
            post.instance.author = request.user
            post.save()
            return redirect('add_post')
    else:
        post = forms.PostForm()
    return render(request, 'posts/post.html', {'post': post})


@login_required
def edit_post(request, id):
    post_forms = Post.objects.get(pk=id)
    post = forms.PostForm(instance=post_forms)
    if request.method == 'POST':
        post = forms.PostForm(request.POST, instance=post_forms)
        if post.is_valid():
            post.instance.author = request.user
            post.save()
            return redirect('profile')

    return render(request, 'posts/post.html', {'post': post})


@login_required
def delete_post(request, id):
    post_forms = Post.objects.get(pk=id)
    post_forms.delete()
    return redirect('home')
