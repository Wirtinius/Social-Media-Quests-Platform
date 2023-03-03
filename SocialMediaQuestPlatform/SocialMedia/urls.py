from django.urls import path 
from .views import *

urlpatterns = [
    path("", home, name="home"),

    # Authentication
    path("register/", registerPage, name="register"),
    path("login/", loginPage, name="login"),
    path("logout/", logoutPage, name="logout"),

    # User
    path("post-form/", postForm, name="post-form"),
    path("profile-form/<str:pk>/", userProfileForm, name="profile-form"),
    path("user-post/<str:pk>", UserPost, name="user-post"),
    path("post-change/<str:pk>/", postChange, name="post-change"),
    path("post-delete/<str:pk>/", postDelete, name="post-delete"),
    path("all-users/", AllUsers, name="all-users"),

    # Follow
    path("follow/<str:pk>", follow, name="follow"),
    path("unfollow/<str:pk>", unfollow, name="unfollow"),

    # Chat
    path("chat/<str:pk>", message, name="chat"),


    # Reaction
    path("like/<str:pk>", like, name="like"),
    path("unlike/<str:pk>", unlike, name="unlike"),

]