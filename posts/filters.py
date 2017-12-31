# from django.contrib.auth.models import User
from .models import Post
import django_filters
from django.db.models import Q


class PostFilter(django_filters.FilterSet):

    message = django_filters.CharFilter(lookup_expr='icontains')
    group = django_filters.CharFilter(lookup_expr='name__icontains')

    class Meta:
        model = Post
        fields = ['message', 'group', ]