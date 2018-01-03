from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify
import misaka
from django.contrib.auth import get_user_model
from django import template
from accounts.models import User


# Create your models here.
AuthUser = get_user_model()
# AuthUser = User
register = template.Library()


class Group(models.Model):
    image_url = models.URLField(default="http://via.placeholder.com/200x200")
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, blank=True, default='')
    members = models.ManyToManyField(AuthUser, related_name='group_members', through='GroupMember')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug':self.slug})

    class Meta:
        ordering = ['name']


class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name='memberships')
    user = models.ForeignKey(AuthUser, related_name='user_group')

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')
