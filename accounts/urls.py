from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import signup

app_name = 'accounts'

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('sign-up', signup, name='sign-up'),   
]