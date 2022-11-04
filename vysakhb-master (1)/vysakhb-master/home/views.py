from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def index(requesst):          
    blogsdata =Blog.objects.all()
    context={"blogs" : blogsdata}
    return render(requesst, "index.html", context=context)
    
