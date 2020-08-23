# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from chartit import DataPool, Chart
from django.db.models import Avg, Sum, Count, Min, Max
from .models import Experience, Education, TechnicalSkills, SocialMedia, Projects
from django.shortcuts import render, get_object_or_404


def homepage(request):
    tech_skills= DataPool(series=[{'options': {'source':TechnicalSkills.objects.filter(category__iexact="Technical")},'terms':[{'skills':'skills','scale':'scale'}]}])
    Personl_skills=DataPool(series=[{'options': {'source':TechnicalSkills.objects.filter(category__iexact="Personal")},'terms':[{'skills':'skills','scale':'scale'}]}])
    def monthname(skills):
        return skills
    cht=Chart(
        datasource=tech_skills,
        series_options=[{'options':{'type': 'column','stacking': False },'terms':{'skills':['scale']}}],
        chart_options=
        {"title":{"text": "Expertise in Technical Languages"},
            "xAxis":{"title":{"text":"Skills"}},
            "yAxis":{"title":{"text":"Scale ( 1- 10 )"}},
            "legend":{"enabled":True},
            "credits":{"enabled":True}},
        x_sortf_mapf_mts=(None,monthname,False))
    cht2=Chart(
        datasource=Personl_skills,
        series_options=[{'options':{'type': 'column','stacking': False },'terms':{'skills':['scale']}}],
        chart_options=
        {"title":{"text": "Personal development Skillset"},
            "xAxis":{"title":{"text":"Skills"}},
            "yAxis":{"title":{"text":"Scale ( 1- 10 )"}},
            "legend":{"enabled":True},
            "credits":{"enabled":True}},
        x_sortf_mapf_mts=(None,monthname,False))

    experiences=Experience.objects
    educations=Education.objects
    return render(request, "experiences/official_home.html", {'experiences':experiences,'educations':educations,'chart_list':[cht,cht2]})

def personalhomepage(request):
    socialmedia=SocialMedia.objects
    educations=Education.objects
    return render(request, "experiences/personal_home.html",{'socialmedia':socialmedia})

def visteon(request):
    visteon_skills= DataPool(series=[{'options': {'source':TechnicalSkills.objects.filter(category__iexact="Visteon")},'terms':[{'skills':'skills','scale':'scale'}]}])
    def monthname(skills):
        return skills
    cht3=Chart(
        datasource=visteon_skills,
        series_options=
        [{'options':{
            'type': 'pie',
             'plotBorderWidth': 1,
              'zoomType': 'xy',              
              'legend':{'enabled': True,}},
            'terms':{'skills':['scale']}
            }],
        chart_options=
        {"title":{"text": "Amount of Experience in each skill"},
            "xAxis":{"title":{"text":"Scale"}},
            "yAxis":{"title":{"text":"Skills"}},
            "legend":{"enabled":True},
            "credits":{"enabled":True}},
        x_sortf_mapf_mts=(None,monthname,False)
            )
    return render(request, "experiences\\visteon.html",{'chart_list':[cht3]})

def zf(request):
    zf_skills= DataPool(series=[{'options': {'source':TechnicalSkills.objects.filter(category__iexact="ZF")},'terms':[{'skills':'skills','scale':'scale'}]}])
    def monthname(skills):
        return skills
    cht3=Chart(
        datasource=zf_skills,
        series_options=
        [{'options':{
            'type': 'pie',
             'plotBorderWidth': 1,
              'zoomType': 'xy',              
              'legend':{'enabled': True,}},
            'terms':{'skills':['scale']}
            }],
        chart_options=
        {"title":{"text": "Amount of Experience in each skill"},
            "xAxis":{"title":{"text":"Scale"}},
            "yAxis":{"title":{"text":"Skills"}},
            "legend":{"enabled":True},
            "credits":{"enabled":True}},
        x_sortf_mapf_mts=(None,monthname,False)
            )
    return render(request, "experiences\\zf.html",{'chart_list':[cht3]})


class Student(ListView):
    template_name="experiences/student.html"
    def get_queryset(self):
        return Education.objects.all()

class AcademicProjects(ListView):
    template_name="experiences/academicprojects.html"
    def get_queryset(self):
        return Projects.objects.filter(category__iexact="Project")

class Papers(ListView):
    template_name="experiences/papersworkshops.html"
    def get_queryset(self):
        return Projects.objects.all()




