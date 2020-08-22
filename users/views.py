from django.shortcuts import render
from django.views.generic import ListView
from users.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin


class Profile_List(LoginRequiredMixin, ListView):
    model = Profile
    context_object_name = 'profile'
