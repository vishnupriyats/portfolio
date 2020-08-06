from django.shortcuts import render
from django.http import HttpResponse
import mimetypes
import codecs
# Create your views here.

def index(request):
    return render(request,'portfolio_app/index.html',{})


# def education(request):
#     return render(request,'portfolio_app/education.html',{})


# def projects(request):
#     return render(request,'portfolio_app/projects.html',{})


# def skills(request):
#     return render(request,'portfolio_app/skills.html',{})

# def interests(request):
#     return render(request,'portfolio_app/interests.html',{})


