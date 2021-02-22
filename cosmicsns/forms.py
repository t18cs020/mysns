from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm(auth_forms.AuthenticationForm):
    '''ログインフォーム'''
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label

class RegisterForm(UserCreationForm):
 
    # 入力を必須にするため、required=Trueで上書き
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)

    class Meta:
        model = User
 
        fields = (
            "email", "password1", "password2", 
            "username",,
            )
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
 
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'お名前'
 
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレス'

#        self.fields['icon'].widget.attrs['class'] = 'form-control'
#        self.fields['icon'].widget.attrs['placeholder'] = 'アイコン画像'
         
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'パスワード'
  
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'パスワード（確認）'

