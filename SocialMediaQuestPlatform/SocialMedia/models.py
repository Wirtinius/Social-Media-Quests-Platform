from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    bio_info = models.TextField(null=True, blank=True)
    follower = models.ManyToManyField('self', symmetrical=False, related_name='user_follower', null=True) 
    # symmetrical is False to define a One-to-Many relationship between users and their followers/following.
    following = models.ManyToManyField('self', symmetrical=False, related_name='user_following', null=True)
    def __str__(self):
        return self.username


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_name = models.CharField(max_length=30)
    post_description = models.TextField()

    def __str__(self):
        return self.post_name


class Chat(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_sender')
    message = models.TextField()


    def __str__(self):
        return self.message