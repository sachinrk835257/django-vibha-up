from django.shortcuts import render,redirect, HttpResponse

# Create your views here.
def index(request):
    title = '''Vibha UP - Home'''
    return render(request, 'vibhaApp/index.html',{"title":title})

def about(request):
    title = '''Vibha UP - About'''
    return render(request, 'vibhaApp/index.html',{"title":title})
def aims(request):
    title = '''Vibha UP - Home'''
    return render(request, 'vibhaApp/index.html',{"title":title})

def events(request):
    title = '''Vibha UP - Home'''
    return render(request, 'vibhaApp/index.html',{"title":title})

def members(request):
    title = '''Vibha UP - Home'''
    return render(request, 'vibhaApp/index.html',{"title":title})

def membership(request):
    title = '''Vibha UP - Home'''
    return render(request, 'vibhaApp/index.html',{"title":title})

def our_members(request):
    title = '''Vibha UP - Home'''
    return render(request, 'vibhaApp/index.html',{"title":title})

def our_team(request):
    title = '''Vibha UP - Home'''
    return render(request, 'vibhaApp/index.html',{"title":title})

def photo_gallery(request):
    title = '''Vibha UP - Home'''
    return render(request, 'vibhaApp/index.html',{"title":title})

def registration(request):
    title = '''Vibha UP - Home'''
    return render(request, 'vibhaApp/index.html',{"title":title})
