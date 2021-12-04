from django import forms
from authapp.forms import UserRegisterForm, UserProfilerForm
from authapp.models import User


class UserAdminRegisterForm(UserRegisterForm):
    image = forms.ImageField(widget=forms.FileInput, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'image', 'first_name', 'last_name', 'age', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserAdminRegisterForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


class UserAdminProfileForm(UserProfilerForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control py-4', 'readonly':False}))
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control py-4', 'readonly':False}))