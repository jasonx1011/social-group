from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from . import models


class UserCreateForm(UserCreationForm):

    class Meta:
        # fields = ('username', 'email', 'password1', 'password2')
        # fields = ('username', 'password1', 'password2')
        fields = ('username', 'image_url', 'description', 'password1', 'password2')
        # model = get_user_model()
        model = models.User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        # self.fields['email'].label = 'Email Address'
