from django.shortcuts import get_object_or_404, redirect ,render
from django.http import HttpResponse
from .models import Projects,Profile,Reviews
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UpdateProfileForm,UserUpdateform,ReviewsForm,NewPostForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required(login_url = '/accounts/login/')
def home(request):
    current_user = request.user
    projects = Projects.get_all_projects()
    users = User.objects.all()
    
    return render(request,'start/home.html',{"projects":projects,"current_user":current_user,"users":users})
@login_required(login_url = '/accounts/login/')
def profile(request):
    name = request.user
    profile = Profile.get_profile_by_name(name)
    projects= Projects.get_project_by_name(name)

    return render(request,"start/profile.html",{"profile":profile,"projects":projects,"name":name})

@login_required(login_url = '/accounts/login/')   
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
   
@login_required(login_url="/accounts/login/")
def logout(request):
  logout(request)
  return redirect('home')

@login_required(login_url = '/accounts/login/')
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

def post_review(request,id):
    
    form = ReveiwForm()
    reviews = Reviews.get_review_by_project_id(id)
    project = Project_Post.get_project_by_id(id)
    rates = Rates.get_rates_by_project_id(id)
    desrate = []
    usarate=[]
    conrate=[]
    if rates:
        for rate in rates:
            desrate.append(rate.design)
            usarate.append(rate.usability)
            conrate.append(rate.content)
        total = len(desrate)*9
        design =round(sum(desrate)/total *100,2)
        usability = round(sum(usarate)/total *100,2)
        content = round(sum(conrate),2)
        return render(request,'start/viewinfo.html',{"form":form,"reviews":reviews,"project":project,"project_id":id,"design":design,"usability":usability,"content":content})
    else:
        usability=0
        design = 0
        content = 0
        return render(request,'start/viewinfo.html',{"form":form,"reviews":reviews,"project":project,"project_id":id,"design":design,"usability":usability,"content":content})
@login_required(login_url = '/accounts/login/')
def review(request,id):
    
    if request.method =='POST':
        project = get_object_or_404(Projects,id =id)
        form = ReviewsForm(request.POST)

        if form.is_valid():
            projectReviews = form.save(commit = False)
            projectReviews.posted_by = request.user
            project = Projects.objects.get(id = id)
            projectReviews.project_id = project
            projectReviews.save()
            return redirect('home')

    else:
        form =ReviewsForm()
        image = get_object_or_404(Projects,id =id)
        id = image.id
    return render(request,'start/review.html',{"form":form,"id":id})

def review_view(request,id):
  
    project = Projects.objects.filter(id=id)
    reviews = Reviews.objects.filter(project_id = id)
    return render(request,'start/viewinfo.html',{"project":project,"reviews":reviews})

@login_required(login_url = '/accounts/login/')   
def post_rate(request,id):
    if request.method=='POST':
        rates = Rates.get_rates_by_project_id(id)
        for rate in rates:
            if rate.rate_by ==request.user:
                messages.info(request,'You have already rated the project')
                return redirect('post-review', id)
        design = request.POST.get('design')
        usability = request.POST.get('usability')
        content = request.POST.get('content')
        
        if design and usability and content:
            project = Project_Post.objects.get(id=id)
            rate = Rates(design = design,usability = usability,content=content,project_id = project,rate_by=request.user)
            
            rate.save()
            return redirect('home')
      
    return render(request,'start/viewinfo.html')    
    
@login_required(login_url = '/accounts/login/')
def search_results(request):
    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
        searched_name = search_results.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'start/search.html',{"message":message,"name": searched_name})

    else:
        message = "You haven't searched for any term"
        return render(request, 'start/search.html',{"message":message})
        
        
        
        
        
    
    