from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from datetime import datetime


def query():
    result = Post.objects.select_related(
        'category',
        'author',
        'location'
    ).filter(
        is_published=True,
        pub_date__lt=datetime.now(),
        category__is_published=True
    )

    return result


def index(request):
    post_list = query().order_by('-pub_date')[:5]

    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    post = get_object_or_404(
        query(),
        pk=post_id
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category.objects.filter(is_published=True),
        slug=category_slug
    )
    post_by_category = query().filter(
        category__slug=category_slug
    )
    return render(request, 'blog/category.html',
                  {'category': category, 'post_list': post_by_category})
