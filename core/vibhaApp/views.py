from django.shortcuts import render,redirect, HttpResponse

from django.contrib import messages

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
    if request.method == 'POST':
        membershipPrice = request.POST.get('membershipPrice')
        selectStatus = request.POST.get('selectStatus')
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        areaOfInterest = request.POST.get('areaOfInterest')
        otherInterest = ""
        if areaOfInterest == "Other":
            otherInterest = request.POST.get('otherInterest')
        
        instituteName = request.POST.get('instituteName')
        designation = request.POST.get('designation')
        priEmail = request.POST.get('pri-email')
        priMobile = request.POST.get('pri-mobile')
        priWhatsapp = request.POST.get('pri-whatsapp')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 != pass2:
            messages.add_message(request, messages.INFO, "PASSWORD NOT MATCH!!")
            return redirect('http://127.0.0.1:8000/registration/') 
        
        countrySelect = request.POST.get('countrySelect')
        selectState = request.POST.get('selectState')
        selectCity = request.POST.get('selectCity')
        pinCode = request.POST.get('pinCode')
        postAddress = request.POST.get('postAddress')
        print("***")
        print(membershipPrice,selectStatus,name,gender,dob,areaOfInterest,otherInterest,instituteName,designation,priEmail,priMobile,priWhatsapp,pass1,pass2,countrySelect,selectState,selectCity,pinCode,postAddress)
        print("***")
        # membershipPrice = request.POST.get('membershipPrice')
        # membershipPrice = request.POST.get('membershipPrice')


    return render(request, 'vibhaApp/registration.html',{"title":title})

def contact(request):
    title = '''Vibha UP - Contact Us'''
    return render(request, 'vibhaApp/contact-us.html',{"title":title})
