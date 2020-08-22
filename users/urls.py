from django.urls import path
from users import views


urlpatterns = [
    path('', views.Profile_List.as_view(), name='profile')
]
