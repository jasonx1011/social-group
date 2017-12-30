from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView
from braces.views import SelectRelatedMixin
from . import forms
from . import models


# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class Profile(ListView):
    model = models.User
    template_name = "accounts/profile.html"


class AccountList(ListView):
    model = models.User
    template_name = "accounts/account_list.html"


