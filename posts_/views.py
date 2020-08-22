from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from users.models import Profile
from django.views import View


class Instagram_Home(LoginRequiredMixin, View):
    def get(self, request):
        context_object_name = {
            'profile': Profile
        }
        template_name = 'posts_/insta_home.html'
        return render(request, template_name, context_object_name)
