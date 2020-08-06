from django.shortcuts import render
from django.http import HttpResponse
import mimetypes
import codecs
# Create your views here.

def index(request):
    return render(request,'portfolio_app/index.html',{})


def education(request):
    return render(request,'portfolio_app/education.html',{})


def projects(request):
    return render(request,'portfolio_app/projects.html',{})


def skills(request):
    return render(request,'portfolio_app/skills.html',{})

def interests(request):
    return render(request,'portfolio_app/interests.html',{})


def download_file(request):
    # fill these variables with real values
    fl_path = 'static\images\Resume.pdf'
    filename = 'Resume.pdf'

    fl = codecs.open(fl_path,'r',encoding='utf8',errors='ignore')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
