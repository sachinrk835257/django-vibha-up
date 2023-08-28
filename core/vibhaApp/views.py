from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.models import User
from vibhaApp.models import Registration, Email_Verification
from django.conf import settings
# from vibhAuth import email_verify
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
        membershipPrice = request.POST.get('Membership ')
        selectStatus = request.POST.get('Select-Status')
        name = request.POST.get('Name')
        gender = request.POST.get('Gender')
        dob = request.POST.get('DOB')
        areaOfInterest = request.POST.get('Area-Of-Interest')       
        otherInterest = ""        
        instituteName = request.POST.get('Institute-Name')
        designation = request.POST.get('Designation')
        priEmail = request.POST.get('Primary-Email')
        priMobile = request.POST.get('Primary-Mobile')
        priWhatsapp = request.POST.get('Primary-WhatsApp')
        pass1 = request.POST.get('Pass1')
        pass2 = request.POST.get('Pass2')

        if areaOfInterest == "Other":
            otherInterest = request.POST.get('Other-Interest')

        if pass1 != pass2:
            messages.add_message(request, messages.INFO, "PASSWORD NOT MATCH!!")
            return redirect('http://127.0.0.1:8000/registration/') 
        
        if Registration.objects.filter(primary_email = primary_email,primary_mobile = primary_mobile).exists():
            messages.add_message(request, messages.WARNING, "USER IS ALREADY EXIST")
            return redirect('http://127.0.0.1:8000/registration/') 
        
        countrySelect = request.POST.get('Country')
        selectState = request.POST.get('State')
        selectCity = request.POST.get('City')
        pinCode = request.POST.get('Pin-Code')
        postAddress = request.POST.get('Postal-Address')
        terms = request.POST.get('Accept-Terms')
        print("***")
        print(membershipPrice,selectStatus,name,gender,dob,areaOfInterest,otherInterest,instituteName,designation,priEmail,priMobile,priWhatsapp,pass1,pass2,countrySelect,selectState,selectCity,pinCode,postAddress)
        print("***")
        # membershipPrice = request.POST.get('membershipPrice')
        # membershipPrice = request.POST.get('membershipPrice')



    return render(request, 'vibhaApp/registration.html',{"title":title})

def contact(request):
    title = '''Vibha UP - Contact Us'''
    return render(request, 'vibhaApp/contact-us.html',{"title":title})
