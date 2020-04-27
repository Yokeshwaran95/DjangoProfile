# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Experience, Education

# Create your views here.

def startpage(request):
    return render(request, "experiences/start.html")

def homepage(request):
    experiences=Experience.objects
    educations=Education.objects
    return render(request, "experiences/official_home.html", {'experiences':experiences,'educations':educations})

def personalhomepage(request):
    experiences=Experience.objects
    educations=Education.objects
    return render(request, "experiences/personal_home.html")

def visteon(request):
    i="visteon"
    return render(request, "experiences\\visteon.html")

def zf(request):
    i="visteon"
    return render(request, "experiences\\zf.html")

def student(request):
    i="visteon"
    return render(request, "experiences\\student.html")
def academicprojects(request):
    i="visteon"
    return render(request, "experiences\\academicprojects.html")




