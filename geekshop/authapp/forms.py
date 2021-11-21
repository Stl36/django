from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from authapp.models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegisterForm(UserCreationForm):
    pass
    #
    # class Meta:
    #     model = User
    #     fields = ('')
