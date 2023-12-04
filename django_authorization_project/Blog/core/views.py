from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import Blog

# Create your views here.
def listing(request):
    data = {
        "blogs": Blog.objects.all(),
    }
    return render(request, "listing.html", data)

@login_required
def view_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    data = {
        "blog": blog,
    }
    return render(request, "view_blog.html", data)

def see_request(request):
    text = f"""
    Some atributes of the HttpRequest Object: 

    scheme: {request.scheme}
    path: {request.path}    
    method: {request.method}    
    GET: {request.GET}
    user: {request.user}
    """

    return HttpResponse(text, content_type="text/plain")

@user_passes_test(lambda u: u.is_superuser)
def admin_page(request):
    return HttpResponse("Admin Page")

@login_required
def add_messages(request):
    usrname = request.user.username 
    messages.add_message(request, messages.INFO, f"Hello {usrname}")
    messages.add_message(request, messages.WARNING, f"DANGER")
    return HttpResponse("Messages added", 
                        content_type="text/plain")
