from django.urls import path
from . import views
from django.conf.urls import url



urlpatterns = [
    path('', views.home,name='home'),
    path('project/profile/',views.profile,name="profile"),
    url(r'^updateprofile/$',views.updateprofile,name='updateprofile'),
]