from django.shortcuts import get_object_or_404, redirect ,render
from django.http import HttpResponse
from .models import Projects
from django.contrib import messages
from django.contrib.auth.models import User

def home(request):
    current_user = request.user
    projects = Projects.get_all_projects()
    users = User.objects.all()
    
    return render(request,'start/home.html',{"projects":projects,"current_user":current_user,"users":users})

def profile(request):
    name = request.user
    profile = Profile.get_profile_by_name(name)
    photos = Photos.get_photos_by_name(name)

    return render(request,"profile.html",{"profile":profile,"photos":photos,"name":name})
    
def updateprofile(request):
   
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)
        form1 = UserUpdateform(request.POST,instance=request.user)
        if form.is_valid() and form1.is_valid():
            form1.save() 
            form.save()
            return redirect('profile')
    else:
        form = UpdateProfileForm(instance=request.user.profile)
        form1 = UserUpdateform(instance=request.user)
    return render(request,"updateprofile.html",{"form":form,"form1":form1})
   
