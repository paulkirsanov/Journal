from django.urls import path
from blog.views import index, about, show_post

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('post/<int:post_id>/', show_post, name='post'),
    #path('post/<slug:post>/', show_post, name='post'),
]
