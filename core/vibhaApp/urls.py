
from django.urls import path, include
from vibhaApp import views

urlpatterns = [
    path('', views.index , name="go to vibha App"),
    path('about/',views.about, name="about page"),
]