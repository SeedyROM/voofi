from django.db import models
from django.contrib.auth.models import User


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Post(models.Model):
    body = models.CharField(max_length=256)
    posted_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    reply = models.ForeignKey('posts.Post', null=True, on_delete=models.CASCADE, related_name='replies')
    likes = models.ManyToManyField(Like, related_name='post')

    def __str__(self):
        return f'{self.user.username}: {self.body[:50]}...'

    class Meta:
        ordering = ['-posted_at',]
