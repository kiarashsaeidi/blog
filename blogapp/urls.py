from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name="starting"), 
    path("posts/<slug:slug>", views.posts, name = "posts"), 
    path("posts/", views.allposts, name="all-posts")
]
