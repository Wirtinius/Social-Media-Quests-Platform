from django.urls import path 
from .views import home, registerPage, loginPage, logoutPage, userProfileForm, postForm, UserPost, postChange, postDelete, follow, unfollow

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

    # Follow
    path("follow/<str:pk>", follow, name="follow"),
    path("unfollow/<str:pk>", unfollow, name="unfollow")
]