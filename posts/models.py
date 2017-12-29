from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from groups.models import Group
from django.contrib.auth import get_user_model

import misaka

# Create your models here.
User = get_user_model()


class Post(models.Model):
    image_url = models.URLField(default="http://via.placeholder.com/140x100")
    user = models.ForeignKey(User, related_name='posts')
    created_at = models.DateTimeField(auto_now=True)
    # image = models.ImageField(upload_to='documents/')
    # image_url = models.URLField()
    # image_url = models.TextField()
    message = models.TextField(blank=True, default="")
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name='posts', null=True, blank=True)
    postlike_members = models.ManyToManyField(User, related_name='postlike_members', through='PostLike')

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:single', kwargs={'username': self.user.username,
                                               'pk': self.pk})

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'message']


class PostLike(models.Model):
    post = models.ForeignKey(Post, related_name='post_liked')
    user = models.ForeignKey(User, related_name='user_like')

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('post', 'user')