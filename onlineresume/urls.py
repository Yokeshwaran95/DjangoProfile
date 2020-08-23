"""onlineresume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import experiences.views
from django.conf import settings
from django.conf.urls.static import static
from experiences.views import ( Student,AcademicProjects,Papers )
from charts.views import sales

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', experiences.views.personalhomepage, name='home'),
    url(r'charts/', sales, name='charts'),
    url(r'official/', experiences.views.homepage, name='official_home'),
    # url(r'personal/', experiences.views.personalhomepage, name='personal_home'),
    url(r'experiences/visteon/', experiences.views.visteon, name='visteon'),
    url(r'experiences/zf/', experiences.views.zf, name='zf'),
    url(r'experiences/zion/', Student.as_view(), name='zion'),
    url(r'academic-projects/', AcademicProjects.as_view(), name='academicprojects'),
    url(r'papers-workshops/', Papers.as_view(), name='papers-workshops'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)