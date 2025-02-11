from django.shortcuts import render, get_object_or_404
# from django.db.models import Q
from blog.models import Post, Category
from datetime import datetime


def index(request):
    post_list = Post.objects.filter(
        pub_date__lt=datetime.now(),
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[0:5]
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    post = get_object_or_404(
        Post.objects.filter(
            pub_date__lt=datetime.now(),
            is_published=True,
            category__is_published=True
        ),
        pk=post_id
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category.objects.filter(is_published=True),
        slug=category_slug
    )
    post_by_category = Post.objects.filter(
        category__slug=category_slug,
        is_published=True,
        pub_date__lt=datetime.now()
    )
    return render(request, 'blog/category.html',
                  {'category': category, 'post_list': post_by_category})
