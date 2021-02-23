from django.urls import path
from . import views
app_name='cosmicsns'
urlpatterns = [
    path('list/', views.PostsList.as_view(),name='list'),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('create/', views.UserCreateView.as_view(),name="create"),
    path('tweet/', views.TweetView.as_view(),name="tweet"),
    path('userinfo/<int:pk>', views.UserInfoView.as_view(),name='userinfo'),
    path('useredit/<int:pk>', views.UserEditView.as_view(),name='useredit'),
]
