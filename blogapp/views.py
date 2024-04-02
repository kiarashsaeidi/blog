from django.shortcuts import render

from .models import Posts, Author, tag


def index(request):
    
    recent_posts = Posts.objects.all().order_by("-date")[:3]
    
    return render(request, "index.html" , {
        "posts" : recent_posts
    })
    # return HttpResponse("hello")

def posts(request, slug): 

    selected_post = Posts.objects.get(slug = slug)
    return render(request, "post-detail.html", {
        "post" : selected_post
    })

def allposts(request):
    return render(request, "all-posts.html", {
        "all_post" : Posts.objects.all()
    })

# Create your views here.
