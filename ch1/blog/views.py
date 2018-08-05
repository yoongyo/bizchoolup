import os
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView

from . models import Post,Category
from .forms import PostForm

def category_list(request):
    qs1 = Category.objects.all()
    return render(request, 'blog/category_list.html', {
        'category_list': qs1,
    })



def post_list(request, category):
    qs1 = Category.objects.all()
    qs = Post.objects.all()
    qs = qs.filter(category__name=category)
    return render(request, 'blog/post_list.html', {
        'post_list': qs,
        'category_list': qs1,
    })



def post_detail(request, category, title):
    qs1 = Category.objects.all()
    qs = get_object_or_404(Post, title=title)
    return render(request, 'blog/post_detail.html', {
        'post_detail': qs,
        'category_list': qs1,
    })


def post_new(request):
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else:
        form = PostForm()

    return render(request, 'blog/post_new.html', {
        'form': form
    })


def post_edit(request, category, title):
    foi = Post.objects.all()
    foi = foi.filter(title=title)
    post1 = get_object_or_404(Post, title=title)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post1)
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else:
        form = PostForm(instance=post1)

    return render(request, 'blog/post_edit.html', {
        'form': form,
        'post': foi,
    })


