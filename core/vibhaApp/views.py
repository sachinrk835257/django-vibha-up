from django.shortcuts import render,redirect, HttpResponse

# Create your views here.
def index(request):
    title = '''Vibha UP - Home'''
    return render(request, 'vibhaApp/index.html',{"title":title})

def about(request):
    title = '''Vibha UP - About'''
    return render(request, 'vibhaApp/about.html',{"title":title})
def aims(request):
    title = '''Vibha UP - Home'''
    return render(request, 'vibhaApp/aims.html',{"title":title})

def events(request):
    title = '''Vibha UP - Events'''
    return render(request, 'vibhaApp/events.html',{"title":title})

def members(request):
    title = '''Vibha UP - Members'''
    return render(request, 'vibhaApp/members.html',{"title":title})

def membership(request):
    title = '''Vibha UP - Membership'''
    return render(request, 'vibhaApp/membership.html',{"title":title})

def our_members(request):
    title = '''Vibha UP - Our Members'''
    return render(request, 'vibhaApp/our-members.html',{"title":title})

def our_team(request):
    title = '''Vibha UP - Our Team'''
    return render(request, 'vibhaApp/our-team.html',{"title":title})

def photo_gallery(request):
    title = '''Vibha UP - Photo Gallery'''
    return render(request, 'vibhaApp/photo-gallery.html',{"title":title})

def registration(request):
    title = '''Vibha UP - Registration'''
    return render(request, 'vibhaApp/registration.html',{"title":title})

def contact(request):
    title = '''Vibha UP - Contact Us'''
    return render(request, 'vibhaApp/contact-us.html',{"title":title})
