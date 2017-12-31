from django.conf.urls import url
from . import views
from django_filters.views import FilterView
from .filters import PostFilter

app_name = 'posts'

urlpatterns = [
    url(r'^$', views.PostList.as_view(), name='all'),
    url(r'new/$', views.CreatePost.as_view(), name='create'),
    url(r'by/(?P<username>[-\w]+)/$', views.UserPosts.as_view(), name='for_user'),
    url(r'by/(?P<username>[-\w]+)/(?P<pk>\d+)/$', views.PostDetail.as_view(), name='single'),
    url(r'update/(?P<pk>\d+)/$', views.UpdatePost.as_view(), name='update'),
    url(r'delete/(?P<pk>\d+)/$', views.DeletePost.as_view(), name='delete'),
    # url(r'^search/$', FilterView.as_view(filterset_class=PostFilter,
    #                                      template_name='posts/post_search.html'), name='search'),
    url(r'^search/$', views.search, name='search')
]
