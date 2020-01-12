from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Projects(models.Model):
    picture = models.ImageField(upload_to= 'media/')
    name = models.CharField(max_length=50)
    details = models.TextField(blank=True)
    createdby = models.CharField(max_length=50,blank=True)
    date_created =  models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    

    @classmethod
    def get_all_projects(cls):
        projects = cls.objects.all()
        return projects

    @classmethod
    def get_project_by_name(cls,name):
        projects = cls.objects.filter(name= name)
        return projects       
     
    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()
        
        
class Profile(models.Model):
    user  = models.OneToOneField(User, on_delete = models.CASCADE, default='')
    profile_pic = models.ImageField(upload_to = 'media/', default='default.jpg')
    bio =models.TextField()
    updated_on = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return f'{self.user.username} profile'
    
    def search_user(cls,username):
        
        found_user = User.objects.get(user= user)

    def save_profile(self):
        
        self.save()

    @classmethod
    def get_profile_by_name(cls,name):
       
        profile = cls.objects.filter(user = name)

        return  name 
    
    
class Reviews(models.Model):
    reviews  = models.CharField(max_length=500)
    date =  models.DateTimeField(auto_now_add=True)
    project_id = models.ForeignKey(Projects,on_delete= models.CASCADE)       
    def __str__(self):
        return self.user

    @classmethod
    def get_all_reviews(cls,id):
        reviews = cls.objects.filter(picture_id=id)
        return reviews

    def save_review(self):
        self.save()

    def delete_review(self):
        self.delete()
          