from django.contrib import admin
from .models import User, Post, Chat, Like
# Register your models here.
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Chat)
admin.site.register(Like)