from django.urls import path    
from django.contrib.auth.decorators import login_required


from . import views

urlpatterns = [
    path("",views.test, name= "starting"), 

    # path("post/", views.Detail.as_view(), name = "detail_post"),
    path("favourites", views.fav, name = "fav"), 
    path("favourite", views.favourite, name= "favourite"),
    path("write", views.write.as_view(), name= "write"),
    # path('register/', views.register, name='register'),
    path('phoeslist', views.phoneslist , name = 'phoneslist'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    

    path("<slug:slugP>", views.Detail.as_view() , name = "detail")
    

    # path("saving-comment", views.SavingComment, name = 'commentsaving'), 
    # path("test", views.trying , name = "try")

]