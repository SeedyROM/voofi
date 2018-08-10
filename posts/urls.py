from django.urls import path

from .views import detail, create, like, likes, unlike

app_name = 'posts'
urlpatterns = [
    path('<int:pk>', detail, name='detail'),
    path('like/<int:pk>', like, name='like'), 
    path('unlike/<int:pk>', unlike, name='unlike'),    
    path('likes/<int:pk>', likes, name='likes'),
    path('create', create, name='create'),    
]