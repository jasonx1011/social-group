from django.db import models
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.utils.text import slugify
import misaka


# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):
    image_url = models.URLField(default="http://via.placeholder.com/140x100")
    description = models.TextField(max_length=80, blank=True, default='')

    def __str__(self):
        return "@{}".format(self.username)

    def get_absolute_url(self):
        return reverse('accounts:profile', kwargs={'pk': self.id})

    class Meta:
        ordering = ['username']
