# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Experience(models.Model):
    image=models.ImageField(upload_to='images/')
    summary=models.CharField(max_length=500)
    description=models.TextField(max_length=1000, null=True, blank=True)
    project=models.TextField(max_length=1000, null=True, blank=True)
    links=models.TextField(max_length=1000,null=True,blank=True)


    def __str__(self):
        return self.summary

class Education(models.Model):
    image=models.ImageField(upload_to='images/')
       # image=models.ImageField(upload_to='images/')
    summary=models.CharField(max_length=500)
    #description=models.TextField(max_length=1000, null=True, blank=True)
    links=models.TextField(max_length=1000,null=True,blank=True)
    def __str__(self):
        return self.summary


class Pictures(models.Model):
    startupimage=models.ImageField(upload_to='images/')
    def __str__(self):
        return self.summary

