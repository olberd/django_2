from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from where_to_go import views
from places import views

urlpatterns = [
    path('', views.index),

]