from django.shortcuts import render
from .models import Profile
import requests
from django.http import HttpResponse

# Create your views here.
def index(request):
    context= {'success':False}
    if request.method =='POST':
        full_name = request.POST['full_name'],
        bio = request.POST['bio'],
        email = request.POST['email'],
        phone = request.POST['phone'],
        
        new_profile = Profile(full_name=full_name, bio=bio, email=email, phone=phone)   
        new_profile.save() 
        # success = 'profile created scucesfully' + full_name
        context={'success':True}
        
        print(new_profile)  
        print(full_name," ", bio," ", email," ", phone)

    return render(request, 'index.html',context)

# def create(request):
#     # context= {'success':False}
    
#         return HttpResponse(context)