from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from core.models import Blog

# Create your views here.

def listing(request):
    data = {
        'blogs': Blog.objects.all()
    }
    return render(request, 'core/listing.html', data)

def view_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    data = {
        'blog': blog
    }  
    return render(request, 'core/view_blog.html', data)

