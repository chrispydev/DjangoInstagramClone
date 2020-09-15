from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from posts_.models import TemPost
from users.models import Profile
from django.views import View


class InstagramHome(LoginRequiredMixin, View):
    @staticmethod
    def get(self, request):
        object_name = {
            'profile': Profile,
        }
        template_name = 'posts_/insta_home.html'
        return render(request, template_name, object_name)


class InstaGet(View):
    @staticmethod
    def get(self, request):
        object_name = {
            'profile': Profile
        }
        return render(request, 'posts_/inst_home.html', object_name)

    @staticmethod
    def post(self, request):
        db = TemPost.objects.create(image=request.FILES['img'])
        form = db.save()
        return redirect('inst_home')


class PrePostList(View):
    def get(self, request):
        posts = TemPost.objects.all()
        last_post = posts.filter().last()
        object_name = {
           'last_post': last_post
        }
        return render(request, 'posts_/insta_post.html', object_name)
