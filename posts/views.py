from django.contrib import messages

from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext

from django.http import Http404
from django.views import generic
from django.db.models import Q

from braces.views import SelectRelatedMixin

from . import models
from . import forms
from .filters import PostFilter

from django.contrib.auth import get_user_model
User = get_user_model()


# def search(request):
#     post_list = models.Post.objects.all()
#     post_filter = PostFilter(request.GET, queryset=post_list)
#     return render(request, 'posts/post_search.html', {'filter': post_filter})

def search(request):
    if request.method == 'GET': # this will be GET now
        in_text = request.GET.get('in_text') # do some research what it does
        try:
            status = models.Post.objects.filter(message__icontains=in_text) # filter returns a list so you might consider skip except part
        except models.Post.DoesNotExist:
            raise Http404
        else:
            return render(request, "posts/post_search.html", {"posts":status})
    else:
        return render(request,"posts/post_search.html",{})
#
#
# class PostSearch(generic.ListView):
#     model = models.Post
#     template_name = "posts/post_search.html"
#
#     paginate_by = 10
#
#     def get_queryset(self):
#         filter_val = self.request.GET.get('filter', '')
#         new_context = models.Post.objects.filter(
#             state=filter_val,
#         )
#         return new_context

#     def get_context_data(self, **kwargs):
#         context = super(PostView, self).get_context_data(**kwargs)
#         context['filter'] = self.request.GET.get('filter', '')
#         return context


# Create your views here.
class PostList(SelectRelatedMixin, generic.ListView):
    model = models.Post
    # paginate_by = 5
    context_object_name = 'posts'
    select_related = ('user', 'group')


class UserPosts(generic.ListView):
    model = models.Post
    template_name = 'posts/user_post_list.html'

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related("posts").get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_user"] = self.post_user
        return context


class PostDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Post
    select_related = ('user', 'group')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))


class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    # form_class = forms.PostForm
    # fields = ('image', 'message', 'group')
    fields = ('image_url', 'message', 'group')
    model = models.Post

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class UpdatePost(LoginRequiredMixin, SelectRelatedMixin, generic.UpdateView):
    fields = ('image_url', 'message', 'group')
    model = models.Post
    template_name_suffix = '_update_form'

    def get_object(self, *args, **kwargs):
        post = get_object_or_404(self.model, pk=self.kwargs['pk'])
        return post


class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Post
    select_related = ('user', 'group')
    success_url = reverse_lazy('posts:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, 'Post Deleted')
        return super().delete(*args, **kwargs)
