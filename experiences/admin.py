# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Experience, Education, TechnicalSkills, SocialMedia, Projects

admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(TechnicalSkills)
admin.site.register(SocialMedia)
admin.site.register(Projects)
# Register your models here.
