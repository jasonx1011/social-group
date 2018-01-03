from django.db import models
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.utils.text import slugify
import misaka


# Create your models here.
# AuthUser = get_user_model()

# class User(models.Model):
class User(auth.models.User, auth.models.PermissionsMixin, models.Model):
    image_url = models.URLField(default="http://via.placeholder.com/200x200")
    description = models.TextField(blank=True, default='')
    relationships = models.ManyToManyField('self', through='Relationship',
                                           symmetrical=False,
                                           related_name='related_to')

    def __str__(self):
        return "@{}".format(self.username)

    def get_image_url(self):
        return self.image_url

    def get_absolute_url(self):
        return reverse('accounts:profile', kwargs={'pk': self.id})

    def add_relationship(self, person, status):
        relationship, created = Relationship.objects.get_or_create(
            from_person=self,
            to_person=person,
            status=status)
        return relationship

    def remove_relationship(self, person, status):
        Relationship.objects.filter(
            from_person=self,
            to_person=person,
            status=status).delete()
        return

    def get_relationships(self, status):
        return self.relationships.filter(
            to_people__status=status,
            to_people__from_person=self)

    def get_related_to(self, status):
        return self.related_to.filter(
            from_people__status=status,
            from_people__to_person=self)

    def get_following(self):
        return self.get_relationships(RELATIONSHIP_FOLLOWING)

    def get_followers(self):
        return self.get_related_to(RELATIONSHIP_FOLLOWING)

    class Meta:
        ordering = ['username']


RELATIONSHIP_FOLLOWING = 1
RELATIONSHIP_BLOCKED = 2
RELATIONSHIP_STATUSES = (
    (RELATIONSHIP_FOLLOWING, 'Following'),
    (RELATIONSHIP_BLOCKED, 'Blocked'),
)


class Relationship(models.Model):
    from_person = models.ForeignKey(User, related_name='from_people')
    to_person = models.ForeignKey(User, related_name='to_people')
    status = models.IntegerField(choices=RELATIONSHIP_STATUSES)



