# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

Category=(
    ("Technical","Technical"),
    ("Personal","Personal"),
    ("ZF","ZF"),
    ("Visteon","Visteon"))

choices=(
    ("Project","Project"),
    ("Papers","Papers"),
    ("Workshops","Workshops"))


class Experience(models.Model):
    image=models.ImageField(upload_to='images/')
    name=models.CharField(max_length=300,default="Freelancer",null=True)
    summary=models.CharField(max_length=500)
    description=models.TextField(max_length=1000, null=True, blank=True)
    project=models.TextField(max_length=1000, null=True, blank=True)
    links=models.TextField(max_length=1000,null=True,blank=True)


    def __str__(self):
        return self.summary

class Education(models.Model):
    image=models.ImageField(upload_to='images/')
    name=models.CharField(max_length=300,default="Academic",null=True)
    Qualifications=models.CharField(max_length=100,null=True,)
    Percentage=models.CharField(max_length=100,null=True,)
    Description=models.CharField(max_length=1000,null=True,)
    start_year = models.PositiveSmallIntegerField(blank=True, null=True)
    end_year=models.PositiveSmallIntegerField(blank=True, null=True)
    links=models.TextField(max_length=1000,null=True,blank=True)
    def __str__(self):
        return self.Qualifications

    def get_description(self):
        # print(self.Description.split(","))
        return self.Description.split(',')


class Pictures(models.Model):
    startupimage=models.ImageField(upload_to='images/')
    def __str__(self):
        return self.summary


class TechnicalSkills(models.Model):
    skills=models.CharField(max_length=100)
    scale=models.IntegerField()
    category=models.CharField(max_length=20,choices=Category,default="Technical")

    def __str__(self):
        return self.skills

class SocialMedia(models.Model):
    name=models.CharField(max_length=300,default=None,null=True)
    app=models.CharField(max_length=100)
    link=models.TextField(max_length=1000,null=True, blank=True)
    pictures=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.app

class Projects(models.Model):
    name=models.CharField(max_length=300)
    Description=models.TextField()
    link=models.TextField(max_length=1000,null=True, blank=True)
    category=models.CharField(max_length=20,choices=choices,default="Papers")

    def __str__(self):
        return self.name

    def get_description(self):
        # print(self.Description.split(","))
        return self.Description.split('.')


