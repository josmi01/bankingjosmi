from django.shortcuts import render,get_object_or_404
from .models import Branches, Places
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views

def allBranches(request,c_slug=None):
    c_page=None
    places=None
    if c_slug!=None:
        c_page=get_object_or_404(Branches,slug=c_slug)
    #     place=Places.objects.all().filter(branch=c_page,available=True)
    # else:
    #     place=Places.objects.all().filter(available=True)
    # paginator = Paginator(place, 6)
    # try:
    #     page=int(request.GET.get('page','1'))
    # except:
    #     page=1
    # try:
    #     place=paginator.page(page)
    # except (EmptyPage,InvalidPage):
    #     place=paginator.page(paginator.num_pages)
    return render(request,'branches.html',{'branch':c_page})

# def placedetail(request,c_slug,place_slug):
#     try:
#         place=Places.objects.get(branch__slug=c_slug,slug=place_slug)
#     except Exception as e:
#         raise e
#     return render(request,'places.html',{'place':place})
def home(request):
    return render(request,'home.html')
def nav(request):
    return render(request,'nav.html')
def register(request):
    return render(request,'register.html')







