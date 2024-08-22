from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
# Create your views here.


def add_category(request):
    if request.method == 'POST':
        category = forms.CategoryForm(request.POST)
        if category.is_valid():
            category.save()
            return redirect('add_category')
    else:
        category = forms.CategoryForm()
    return render(request, 'categories/category.html', {'category': category})
