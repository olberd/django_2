from django.urls import path
from places import views

urlpatterns = [
    path('', views.index),
    path('places/<int:place_id>/', views.place_detail, name='places')

]