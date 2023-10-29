from django.shortcuts import render


# Create your views here.
###### GEtting an error here
def dashboard(request):
    return render(request, "users/dashboard.html")
