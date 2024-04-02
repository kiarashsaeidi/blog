from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from .models import posts, comment
from django.http import HttpResponseRedirect, HttpResponse
from .forms import commentForm
from django.views.generic import FormView
from .formpost import postForm
from django.shortcuts import render 
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login, logout 
from django.contrib import messages 
from django.contrib.auth.decorators import login_required 
from django.utils.decorators import method_decorator






# Create your views here.


def test(request): 

    post = posts.objects.all().order_by("-date")
    return render(request, "index.html", { 
        'post' : post[0], 'post1' : post[1], 'post2': post[2]
    })

# def Detail(): 
#     pass

    # post = posts.objects.filter(slug = slug)[0]
    # comments_specified = comment.objects.filter(post__pk = post.pk)
    # print(post.pk)
    # print(comments_specified)

    
    # return render(request, "Detail.html", { 
    #     'post' : post, 'form': commentForm, 'comments_sp': comments_specified
    # })

class Detail(View):


    def post(self, request, slugP): 
        form_comment = commentForm(request.POST)
        post_id = request.POST['background']
        post_sp = posts.objects.get(pk = post_id)

        if form_comment.is_valid():

            print("I'm here !")
            print(form_comment.cleaned_data)
            print(post_sp.title_m)
            comment_saving_post = form_comment.save(commit=False)
            comment_saving_post.post = post_sp
            comment_saving_post.save() 
            return HttpResponseRedirect(reverse('detail', args=[post_sp.slug]))
    
    def get(self, request, slugP): 
        form = commentForm
        post = posts.objects.get(slug = slugP)

        comments = comment.objects.filter(post__pk = post.pk)
        fav_ids = request.session.get("fav_ids")
        print(fav_ids)
        if fav_ids is None: 
            is_fav = False
        elif (str(post.pk) in fav_ids) : 
            is_fav = True
        else: 
            is_fav = False

        return render(request,"Detail.html", {
            'form': form , 'post' : post, 'comments_sp': comments , "is_fav": is_fav
        })
    


def fav(request): 
    fav_ids = request.session.get("fav_ids")

    if fav_ids is None:
        fav_ids = []


    fav_id = request.POST['fav_id']

    if fav_id not in fav_ids:
        fav_ids.append(fav_id)

    request.session['fav_ids'] = fav_ids
    
    
    return HttpResponseRedirect(reverse("starting"))


def favourite(request): 
    stored_posts = request.session.get("fav_ids")
    context=  {}

    if stored_posts is None or len(stored_posts) == 0: 
        context['posts'] = []
        context['has_posts'] = False

    else: 
        fav_posts = posts.objects.filter(id__in = stored_posts) 
        context['posts'] = fav_posts
        context['has_posts'] = True


    return render(request, "favourite.html", { 
        "posts" : context['posts'], "has_posts" : context['has_posts']
    })


@method_decorator(login_required(login_url='login'), name='dispatch')
class write(FormView): 
    form_class = postForm
    template_name = "write.html"
    success_url = "/"

    def form_valid(self, form): 
        form.save() 
        return super().form_valid(form)
    

# def register(request):
#     if request.user.is_authenticated:
#         print("User is authenticated")
#         return redirect('write')
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         if len(password) < 3:
#             messages.error(request, 'Password must be at least 3 characters')
#             return redirect('register')

#         get_all_users_by_username = User.objects.filter(username=username)
#         if get_all_users_by_username:
#             messages.error(request, 'Error, username already exists, User another.')
#             return redirect('register')

#         new_user = User.objects.create_user(username=username, email=email, password=password)
#         new_user.save()

#         messages.success(request, 'User successfully created, login now')
#         return redirect('login')
#     return render(request, 'todoapp/register.html', {})
    





def LogoutView(request):
    logout(request)
    return redirect('starting')

def loginpage(request):
    if request.user.is_authenticated:
        print("User is authenticated")
        return redirect('write')
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')

        validate_user = authenticate(username=username, password=password)
        if validate_user is not None:
            login(request, validate_user)
            return redirect('write')
        else:
            messages.error(request, 'Error, wrong user details or user does not exist')
            return redirect('login')


    return render(request, 'todoapp/login.html', {})





def phoneslist(request):
    phones =  posts.objects.all().order_by('-date')
    return render(request, "phoeslist.html", { 
        'posts': phones
    })



    









# def SavingComment(request):


    # if request.method == 'POST':
    #     form_comment = commentForm(request.POST)
    #     post_id = request.POST['background']
    #     print(post_id)
    #     post_sp = posts.objects.get(pk = post_id)
        
    #     if form_comment.is_valid():

    #         print("I'm here !")
    #         print(form_comment.cleaned_data)
    #         print(post_sp.title_m)
    #         comment_saving_post = form_comment.save(commit=False)
    #         comment_saving_post.post = post_sp
    #         comment_saving_post.save() 

    # return HttpResponse("hello")

