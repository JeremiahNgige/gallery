from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .models import Category, Image, location


def home(request):
    '''
    renders the landing page
    '''
    
    images = Image.objects.all()
    locations = location.get_locations()
    return render(request,'home.html',{'images':images,'locations':locations})
