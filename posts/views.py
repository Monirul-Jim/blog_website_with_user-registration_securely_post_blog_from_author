from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from . import forms
from . models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.utils.decorators import method_decorator

# Create your views here.

# function based views


# @login_required
# def add_post(request):
#     if request.method == 'POST':
#         post = forms.PostForm(request.POST)
#         if post.is_valid():
#             post.instance.author = request.user
#             post.save()
#             return redirect('add_post')
#     else:
#         post = forms.PostForm()
#     return render(request, 'posts/post.html', {'post': post})

# class based views ->add post
@method_decorator(login_required, name='dispatch')
class AddPostCreateViews(CreateView):
    model = Post
    form_class = forms.PostForm
    template_name = 'posts/post.html'
    success_url = reverse_lazy('add_post')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# @login_required
# def edit_post(request, id):
#     post_forms = Post.objects.get(pk=id)
#     post = forms.PostForm(instance=post_forms)
#     if request.method == 'POST':
#         post = forms.PostForm(request.POST, instance=post_forms)
#         if post.is_valid():
#             post.instance.author = request.user
#             post.save()
#             return redirect('profile')

#     return render(request, 'posts/post.html', {'post': post})

@method_decorator(login_required, name='dispatch')
class EditPostView(UpdateView):
    model = Post
    form_class = forms.PostForm
    template_name = 'posts/post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')


# @login_required
# def delete_post(request, id):
#     post_forms = Post.objects.get(pk=id)
#     post_forms.delete()
#     return redirect('home')
@method_decorator(login_required, name='dispatch')
class DeletePostView(DeleteView):
    model = Post
    template_name = 'posts/delete_post.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'


class DetailsPostView(DetailView):
    model = Post
    pk_url_kwarg = 'id'
    template_name = 'posts/post_details.html'
