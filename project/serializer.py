from rest_framework import serializers
from .models import Projects,Profile



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user','profile_pic','bio','updated_on']



class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['picture','name','details','createdby','date_created']
        




