from django.shortcuts import render
from . models import Project

def projects(request):
    projects = Project.objects.all()
    context = {'projects' : projects} 
    return render(request, 'projects/projects.html',context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request,'templates/single-project.html',{'project': projectObj  }) 
