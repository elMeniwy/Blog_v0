from django import forms

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='اسم المستخدم', max_length=30)
    email = forms.EmailField(label='الايميل')
    first_name = forms.CharField(label='الاسم الاول')
    last_name = forms.CharField(label='الاسم الاخير')
    password1 = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput(), min_length=8)
    password2 = forms.CharField(label='تاكيد كلمة المرور', widget=forms.PasswordInput(), min_length=8)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    # def clean_password2(self):
    #     cd = self.cleaned_data
    #     if cd['password1'] != cd['password2']:
    #         raise forms.ValidationError('كلمة المرور غير متطايقة')
    #     return cd['password2'] # return under which field will the message appear
    #
    # def clean_username(self):
    #     cd = self.cleaned_data
    #     if User.objects.filter(username=cd['username']).exists():
    #         raise forms.ValidationError('اسم المستخدم موجود بالفعل')
    #
    #     return cd['username']


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    username = forms.CharField(label='اسم المستخدم', max_length=30)
    password = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput(), min_length=8)


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label='الايميل')
    last_name = forms.CharField(label='الاسم الاخير')
    first_name = forms.CharField(label='الاسم الاول')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)
