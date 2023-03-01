from django.shortcuts import render, redirect
from .models import User, Post
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    user = request.user
    context = {}
    if user.is_authenticated:
        posts = Post.objects.all()
        context = {'posts': posts}
    return render(request, "SocialMedia/home.html", context=context)


# User registration/login/logout/profile
def registerPage(request): 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = make_password(request.POST.get('password'))
        confirm_password = request.POST.get('confirm_password')
        email = request.POST.get('email')
        if not User.objects.filter(username=username) or not User.objects.filter(email=email):
            if check_password(password, confirm_password):
                User.objects.create(username=username, password=password, email=email)
            else:
                messages.error(request, 'The password does not match')
                return redirect('register')
        else: 
            messages.error(request, 'The username or email have already been taken')
            return redirect('register')
        return redirect('home')
    return render(request, "SocialMedia/authentication/register.html")


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credintials')
            return redirect('login')
    return render(request, "SocialMedia/authentication/login.html")

@login_required(login_url='login')
def logoutPage(request):
    logout(request)
    return redirect('home')


# User's interaction
@login_required(login_url='login')
def userProfileForm(request, pk):
    user = User.objects.filter(id=pk)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        second_name = request.POST.get('second_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        personal_info = request.POST.get('personal_info')
        user.update(first_name=first_name, second_name=second_name, username=username, email=email, bio_info=personal_info)
        return redirect('user-post', pk=request.user.id)
    return render(request, "SocialMedia/user/user_profile_form.html")


@login_required(login_url='login')
def postForm(request):
    if request.method == 'POST':
        post_name = request.POST.get('post_name')
        post_description = request.POST.get('post_description')
        if (post_name or post_description) is None: 
            messages.error(request, 'Post should contain both Name and Description!')
            return redirect('post-form')
        Post.objects.create(user=request.user, post_name=post_name, post_description=post_description)
        return redirect('home')
    return render(request, "SocialMedia/user/post_form.html")


@login_required(login_url='login')
def postChange(request, pk):
    post = Post.objects.filter(id=pk)
    post_get = Post.objects.get(id=pk)
    context = {'post': post_get}
    if request.method == 'POST':
        post_name = request.POST.get('post_name')
        post_description = request.POST.get('post_description')
        if (post_name or post_description) is None: 
            messages.error(request, 'Post should contain both Name and Description!')
            return redirect('post-form')
        post.update(post_name=post_name, post_description=post_description)
        return redirect('user-post', pk=request.user.id)
    return render(request, "SocialMedia/user/post_edit.html", context=context)


@login_required(login_url='login')
def UserPost(request, pk):
    is_followed = False
    user = User.objects.get(id=pk)
    posts = user.post_set.all()
    for follower in user.follower.all():
        if follower == request.user:
            is_followed = True
    context = {
        'posts': posts,
        'user_post': user,
        'is_followed': is_followed,
        }
    return render(request, "SocialMedia/user/posts_user.html", context=context)


@login_required(login_url='login')
def postDelete(request, pk):
    post = Post.objects.filter(id=pk)
    post.delete()
    return redirect('user-post')


# Followers
@login_required(login_url='login')
def follow(request, pk):
    # We have two users: the one is the follower(authenticated) and another is the following
    follower = User.objects.get(id=request.user.id)
    following = User.objects.get(id=pk)
    follower.following.add(following)
    following.follower.add(follower)
    return redirect('home')


@login_required(login_url='login')
def unfollow(request, pk):
    # We have two users: the one is the follower(authenticated) and another is the following
    follower = User.objects.get(id=request.user.id)
    following = User.objects.get(id=pk)
    follower.following.remove(following)
    following.follower.remove(follower)
    return redirect('home')