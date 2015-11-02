from django.conf.urls import patterns, include, url
from django.contrib import admin
from testapp import views
urlpatterns = [
    # url(r'', views.testappinwork),
    url(r'^(?P<id>\d+)', views.processed),
]
