from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.views.generic import View
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
# Create your views here.

def posts(request):
    search_query = request.GET.get('search', '')
    
    if search_query:
        page = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        page = Post.objects.all()
    
    paginator = Paginator(page, 3)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''    
    
    return render(
        request,
        'blog/home.html',
        {
        'page': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url,
        }
    )



def post_detail(request, det_slug):
    detail = get_object_or_404(Post, slug=det_slug)
    return render(
        request,
        'blog/post_detail.html',
        {
        'post': detail
        }
    )



class PostCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = PostForm()
        return render(
            request,
            'blog/post_create.html',
            {
            'form': form    
            }
        )
        
    def post(self, request):
        bound_form = PostForm(request.POST)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect('posts_list_url')
        return render(
            request,
            'blog/post_create.html',
            {
            'form': bound_form  
            }
        )


class PostUpdate(LoginRequiredMixin, View):
    def get(self, request, det_slug):
        post = Post.objects.get(slug=det_slug)
        bound_form = PostForm(instance=post)
        return render(
            request,
            'blog/post_update.html',
            {
            'form': bound_form,   
            'post': post
            }
        )
    def post(self, request, det_slug):
        post = Post.objects.get(slug=det_slug)
        bound_form = PostForm(request.POST, instance=post)

        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect('post_detail_url', det_slug=new_post.slug)
        return render(
            request,
            'blog/post_update.html',
            {
            'form': bound_form,
            'post': post
            }
        )


class PostDelete(LoginRequiredMixin, View):
    def get(self, request, det_slug):
        post = Post.objects.get(slug=det_slug)
        return render(
            request,
            'blog/post_delete.html',
            {
            'post': post
            }
        )
        
    def post(self, request, det_slug):
        post = Post.objects.get(slug=det_slug)
        post.delete()
        return redirect(reverse('posts_list_url'))
    

    
def tags_list(request):
    tags = Tag.objects.all()
    alphabet_tags = tags.order_by('title')
    return render(
        request,
        'blog/tags_list.html',
        {
        'tags': alphabet_tags
        }
    )



def tag_detail(request, det_slug):
    tag = get_object_or_404(Tag, slug=det_slug)
    return render(
        request,
        'blog/tag_detail.html',
        {
        'tag': tag,
        }
    )


class TagCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = TagForm()
        return render(
        request,
        'blog/tag_create.html',
        {
        'form': form
        }
    )
        
    def post(self, request):
        bound_form = TagForm(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect('tags_list_url')

        return render(
            request,
            'blog/tag_create.html',
            {
            'form': bound_form  
            }
        )


class TagUpdate(LoginRequiredMixin, View):
    def get(self, request, det_slug):
        tag = Tag.objects.get(slug=det_slug)
        bound_form = TagForm(instance=tag)
        return render(
            request,
            'blog/tag_update.html',
            {
            'form': bound_form,   
            'tag': tag
            }
        )
        
    def post(self, request, det_slug):
        tag = Tag.objects.get(slug=det_slug)
        bound_form = TagForm(request.POST, instance=tag)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect('tag_detail_url', det_slug=new_tag.slug)
        return render(
            request,
            'blog/tag_update.html',
            {
            'form': bound_form,
            'tag': tag
            }
        )



class TagDelete(LoginRequiredMixin, View):
    def get(self, request, det_slug):
        tag = Tag.objects.get(slug=det_slug)
        return render(
            request,
            'blog/tag_delete.html',
            {
            'tag': tag
            }
        )
        
    def post(self, request, det_slug):
        tag = Tag.objects.get(slug=det_slug)
        tag.delete()
        return redirect(reverse('tags_list_url'))
    