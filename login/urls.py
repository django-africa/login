from django.urls import path
from django.contrib.auth.views import LoginView
from .views import HomeView
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login', LoginView.as_view(template_name = 'registration/login.html'), name='login')
]
