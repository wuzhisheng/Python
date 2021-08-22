"""day71xiawu_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from app01 import views as v1
from app02 import views as v2
from app03 import views as v3

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),

    url(r'^app01/login/$', v1.login),
    url(r'^app01/home/$', v1.home),
    url(r'^app01/index/$', v1.index),
    url(r'^app01/logout/$', v1.logout),

    url(r'^app02/login/$', v2.login),
    url(r'^app02/home/$', v2.home),
    url(r'^app02/index/$', v2.index),
    url(r'^app02/logout/$', v2.logout),
    
    url(r'^app03/login/$', v3.login),
    url(r'^app03/index/$', v3.index),
]













