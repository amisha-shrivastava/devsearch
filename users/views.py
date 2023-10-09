from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User 
from . models import Profile


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('profiles')
     
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Invalid Username")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, "Username or Password is incorrect!")
            
    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    messages.success(request, "User successfully logged out!")
    return redirect('login')


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles':profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request,pk):
    profile = Profile.objects.get(id = pk)
    topSkills = profile.skill_set.exclude(description__exact='') #if skill doesnot have description exclude it out
    otherSkills = profile.skill_set.filter(description='')
    context = {'profile':profile, 'topSkills':topSkills,'otherSkills':otherSkills }
    return render(request,'users/user-profile.html', context)

