from django.contrib.auth import views as auth_view
from django.urls import path
from posts_.forms import UserLoginForm
from posts_ import views as posts_view

urlpatterns = [
    path('', auth_view.LoginView.as_view(
        template_name='posts_/insta_login.html', authentication_form=UserLoginForm), name='inst_login'),
    path('inst-home', posts_view.InstagramHome.as_view(), name='inst_home'),
    path('inst-get', posts_view.InstaGet.as_view(), name='inst_get'),
    path('inst-post', posts_view.PrePostList.as_view(), name='inst_post'),
]
