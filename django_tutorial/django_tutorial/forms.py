from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True) # email 필드 추가
    class Meta:
        model = User # 장고 제공 model DB
        fields = ('username', 'email', 'password1', 'password2')