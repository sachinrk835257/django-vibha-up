
from django.urls import path, include
from vibhaApp import views

urlpatterns = [
    path('', views.index , name="go to vibha App"),
    path('about/',views.about, name="about page"),
    path('contact/',views.contact, name="about page"),
    path('aims/',views.aims, name="about page"),
    path('events/',views.events, name="about page"),
    path('members/',views.members, name="about page"),
    path('membership/',views.membership, name="about page"),
    path('our-members/',views.our_members, name="about page"),
    path('our-team/',views.our_team, name="about page"),
    path('photo-gallery/',views.photo_gallery, name="about page"),
    path('registration/',views.registration, name="about page"),
    path('verify/<token>/', views.verify_mail, name="verify mail with unique uuid"),
    path("payment/<id>/", views.order_payment, name="payment"),
    path("razorpay/callback/", views.callback, name="callback")
]