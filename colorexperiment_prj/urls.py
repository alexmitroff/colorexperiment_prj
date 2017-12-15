"""colorexperiment_prj URL Configuration

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
from django.conf.urls import include
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

from experiment import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name="index"),
    url(r'^stimulus/(?P<stimulus_id>\d+)/$', views.stimulus, name="stimulus"),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^logout/$', views.logout_user, name="logout"),
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^api/submit/$', views.submit, name="submit"),
    url(r'^api/change/user/$', views.change_user, name="change_user"),
    url(r'^api/change/user-info/$', views.change_userinfo, name="change_userinfo"),
    url(r'^excel/(?P<stimulus_id>\d+)/$', views.result, name="result"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
