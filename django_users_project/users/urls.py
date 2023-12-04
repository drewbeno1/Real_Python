from django.urls import path, include
from users.views import home, dashboard, register

# There is a line at end of settings file that directs after succesful login
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')), # Don't need a view, django covers us on the functionality
    path("", home, name="home"),
    path("register/", register, name="register")
]