from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse 
from users.forms import CustomUserCreationForm

def home(request):
    return render(request, "users/home.html")

# Create your views here.
def dashboard(request):
    return render(request, "users/dashboard.html")

def register(request):
    # If it's a GET request, we'll just render the form with the context here
    if request.method == 'GET':
        return render(
            request, "registration/register.html",
            {"form": CustomUserCreationForm}
        )
    # If its a POST, a new custom form will be created and the new user will be saved and logged in and redirected to the dashboard
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserCreationForm(request, user)
            return redirect(reverse("dashboard"))