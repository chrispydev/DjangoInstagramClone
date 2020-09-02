from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from posts_.models import Tem_Post
from users.models import Profile
from django.views import View


class Instagram_Home(LoginRequiredMixin, View):
    def get(self, request):
        object_name = {
            'profile': Profile,
        }
        template_name = 'posts_/insta_home.html'
        return render(request, template_name, object_name)


class Insta_Get(View):
    def get(self, request):
        object_name = {
            'profile': Profile
        }
        return render(request, 'posts_/inst_home.html', object_name)

    def post(self, request):
        post_data = request.FILES
        db = Tem_Post.objects.create(image=post_data)
        form = db.save()
        print(form)
        return redirect('inst_home')
