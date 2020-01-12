from django.shortcuts import get_object_or_404, redirect ,render
from django.http import HttpResponse
from .models import Projects,Profile,Reviews
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UpdateProfileForm,UserUpdateform,ReviewsForm,NewPostForm
from django.contrib.auth.decorators import login_required

def home(request):
    current_user = request.user
    projects = Projects.get_all_projects()
    users = User.objects.all()
    
    return render(request,'start/home.html',{"projects":projects,"current_user":current_user,"users":users})

def profile(request):
    name = request.user
    profile = Profile.get_profile_by_name(name)
    projects= Projects.get_project_by_name(name)

    return render(request,"start/profile.html",{"profile":profile,"projects":projects,"name":name})
    
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
    return render(request,"start/updateprofile.html",{"form":form,"form1":form1})
   
# @login_required(login_url="/accounts/login/")
def logout(request):
  
  logout(request)
  return redirect('home')

# @login_required(login_url = '/accounts/login/')
def newpost(request):
    if request.method=='POST':
        form = NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user = request.user
            post.save()

            return redirect('home')

    else:
        form = NewPostForm()
        
    return render(request,'start/newpost.html',{'form':form})


def review(request,id):
    
    if request.method =='POST':
        project = get_object_or_404(Projects,id =id)
        form = CommentForm(request.POST)

        if form.is_valid():
            projectComment = form.save(commit = False)
            projectComment.posted_by = request.user
            project = Projects.objects.get(id = id)
            projectComment.project_id = project
            projectComment.save()
            return redirect('home')

    else:
        form =CommentForm()
        image = get_object_or_404(Projects,id =id)
        id = image.id
    return render(request,'start/review.html',{"form":form,"id":id})

def review_view(request,id):
  
    project = Projects.objects.filter(id=id)
    reviews = Reviews.objects.filter(project_id = id)
    return render(request,'review.html',{"project":project,"reviews":reviews})