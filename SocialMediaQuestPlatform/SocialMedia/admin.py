from django.contrib import admin
from .models import User, Post, Chat, Like, Comment
# Register your models here.
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Chat)
admin.site.register(Like)
admin.site.register(Comment)