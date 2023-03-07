from django.shortcuts import render, redirect
from .models import User, Post, Chat, Like, Comment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def home(request):
    user = request.user
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    if user.is_authenticated:
        posts = Post.objects.all()
        followings = user.following.all()
        context = {
            'posts': posts,
            'followings': followings, 
                   }
    return render(request, "SocialMedia/home.html", context=context)


# User registration/login/logout/profile
def registerPage(request): 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = make_password(request.POST.get('password'))
        confirm_password = request.POST.get('confirm_password')
        email = request.POST.get('email')
        if (username or request.POST.get('password') or confirm_password or email) is None:
            messages.error(request, 'Fill every field to register!')
            return redirect('register')
        else:
            if not User.objects.filter(username=username) or not User.objects.filter(email=email):
                if check_password(confirm_password, password):
                    user = User.objects.create(username=username, password=password, email=email)
                    login(request, user)
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
def userEdit(request, pk):
    user = User.objects.filter(id=pk)
    if request.method == 'POST':
        # first_name = request.POST.get('first_name')
        # second_name = request.POST.get('second_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        user_bio = request.POST.get('user_bio')
        user.update(username=username, email=email, bio_info=user_bio)
        return redirect('user-post', pk=request.user.id)
    return render(request, "SocialMedia/user/edit-user.html")


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
    return render(request, "SocialMedia/user/profile.html", context=context)


@login_required(login_url='login')
def postRoom(request, pk):
    post = Post.objects.get(id=pk)
    comments = post.post_comment.all()
    if request.method == 'POST':
        comment = request.POST.get('comment')
        Comment.objects.create(user=request.user, post=post, comment=comment)
        return redirect('post-room', pk=post.id)
    context = {
        'post': post,
        'comments': comments
               }
    return render(request, "SocialMedia/user/post_room.html", context=context)


@login_required(login_url='login')
def deleteComment(request, pk):
    comment = Comment.objects.get(id=pk)
    post = comment.post
    comment.delete()
    return redirect('post-room', pk=post.id)


@login_required(login_url='login')
def postDelete(request, pk):
    post = Post.objects.filter(id=pk)
    post.delete()
    return redirect('user-post', pk=request.user.id)


@login_required(login_url='login')
def AllUsers(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    user_searched = User.objects.filter(
        Q(username__icontains=q) 
        )


    users = User.objects.all()
    context = {
        'user_searched': user_searched,
        'users': users
    }
    return render(request, "SocialMedia/user/all_users.html", context=context)


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


# Chat
@login_required(login_url='login')
def message(request, pk):
    sender = request.user
    receiver = User.objects.get(id=pk)
    message = request.POST.get('message')
    if request.method == 'POST':
        Chat.objects.create(sender=sender, message=message)
    context={
        'sender': sender,
        'receiver': receiver,
             }    
    return render(request,'SocialMedia/user/chat.html', context=context)


# Reaction
@login_required(login_url='login')
def like(request, pk):
    post = Post.objects.get(id=pk)
    user = request.user
    if user.user_reaction.exists():
        post.post_reaction.update(user=user, post=post, like=True)
    else: 
        Like.objects.create(user=user, post=post, like=True)
    return redirect('home')


@login_required(login_url='login')
def unlike(request, pk):
    post = Post.objects.get(id=pk)
    user = request.user
    user.user_reaction.filter(user=user, post=post).delete()
    return redirect('home')


