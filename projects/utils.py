from django.db.models import Q
from . models import Project, Tag
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



def paginateProjects(request, projects, results):
    page = request.GET.get('page')
    paginator = Paginator(projects, results)
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)
        
    left_index = (int(page)-4)
    if left_index<1:
        left_index=1
    right_index = (int(page)+5)
    if right_index>paginator.num_pages:
        right_index=paginator.num_pages
        
    custom_range = range(left_index,right_index+1)
    return custom_range, projects
    
def searchProjects(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        
    tag = Tag.objects.filter(name__icontains=search_query)
    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query)|
        Q(description__icontains=search_query)|
        Q(owner__name__icontains=search_query)|
        Q(tag__in=tag)
    )
    return projects,search_query