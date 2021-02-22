from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Posts, User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from . import forms
from .forms import RegisterForm
# Create your views here.
class PostsList(LoginRequiredMixin,ListView):
    model = Posts
    template_name = "cosmicsns/posts_list.html"
    def get_queryset(self):
        object_list = Posts.objects.all()
        object_list = object_list.order_by('postedtime')
        object_list = object_list.reverse()
        return object_list
class TweetView(CreateView):
    model = Posts
    fields = ('message',)
    template_name = 'cosmicsns/tweet.html'
    success_url = reverse_lazy('cosmicsns:list')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UserInfoView(LoginRequiredMixin,DetailView):
    model = User
    template_name = "cosmicsns/userinfo.html"
    
class LoginView(LoginView):
    form_class = forms.LoginForm
    template_name = "cosmicsns/login.html"

class LogoutView(LogoutView):
    template_name = "cosmicsns/logout.html"
    
class UserCreateView(CreateView):
    form_class = RegisterForm
    template_name = "cosmicsns/create.html"
    success_url = reverse_lazy("cosmicsns:login")
    
    