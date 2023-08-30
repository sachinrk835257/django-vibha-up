from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.models import User
from vibhaApp.models import Registration, Email_Verification ,Order
from django.conf import settings
# from vibhAuth import email_verify
from vibhaApp.email_otp import send_mail
from django.contrib import messages
from decouple import config
import uuid
import random
import razorpay

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
        membershipPrice = request.POST.get('Membership')
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
        
        # if Registration.objects.filter(primary_email = priEmail,primary_mobile = priMobile).exists():
        #     messages.add_message(request, messages.WARNING, "USER IS ALREADY EXIST")
        #     return redirect('http://127.0.0.1:8000/registration/') 
        
        countrySelect = request.POST.get('Country')
        selectState = request.POST.get('State')
        selectCity = request.POST.get('City')
        pinCode = request.POST.get('Pin-Code')
        postAddress = request.POST.get('Postal-Address')
        terms = request.POST.get('Accept-Terms')
        print("***")
        print(membershipPrice,selectStatus,name,gender,dob,areaOfInterest,otherInterest,instituteName,designation,priEmail,priMobile,priWhatsapp,pass1,pass2,countrySelect,selectState,selectCity,pinCode,postAddress)
        print("***")

        token = str(uuid.uuid4())
        otp = str(random.randint(1000,9999))
        Email_Verification.objects.create(user_uuid = token,user_email = priEmail,user_mobile = priMobile , user_otp = otp)
        
        # membershipPrice = request.POST.get('membershipPrice')
        # membershipPrice = request.POST.get('membershipPrice')
        send_mail(priEmail,otp)
        messages.add_message(request, messages.SUCCESS, "EMAIL SENT SUCCESSFULLY")

        register_obj = Registration.objects.create(accept_terms = terms,membership_fee = membership, dob = dob,district = selectCity, pin_code = pinCode, address = postAddress, state = selectState,country = countrySelect, interest = areaOfInterest, other_interest = otherInterest, full_name = name,institute_name = instituteName,designation =  designation, gender =gender, primary_email = priEmail, primary_mobile = priMobile,primary_whatsapp = priWhatsapp)

        register_obj.save()
        return redirect(f'http://127.0.0.1:8000/verify/{token}') 



    return render(request, 'vibhaApp/registration.html',{"title":title})

def contact(request):
    title = '''Vibha UP - Contact Us'''
    return render(request, 'vibhaApp/contact-us.html',{"title":title})


def verify_mail(request,token):
    print("verification processing.....")
    title = '''Email Verification'''
    user_obj = Email_Verification.objects.filter(user_uuid=token).first()
    print(user_obj)
    if request.method == "POST":
        fetch_otp = request.POST.get('otp')
        if user_obj.user_otp == fetch_otp:
            user_obj.isVerified = True
            register_obj = Registration.objects.get(primary_email = user_obj.user_email)
            print(register_obj.isEmailVerified)
            register_obj.isEmailVerified = True
            user_obj.save()
            print(register_obj.isEmailVerified)
            register_obj.save()
            messages.add_message(request, messages.SUCCESS, "Verification Done")
            # return redirect('http://127.0.0.1:8000/registration/') 
            return HttpResponse("email verification done")
        else:        
            print("fetched otp = ",fetch_otp)
            print("register otp = ",user_obj.user_otp)
            messages.add_message(request, messages.WARNING, "WRONG OTP!!")
            return redirect(f'http://127.0.0.1:8000/verify/{token}') 

    return render(request, 'vibhaAuth/email_otp.html',{"title":title,"email":user_obj.user_email})


def order_payment(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        client = razorpay.Client(auth=(config('RAZORPAY_KEY_ID'), config('RAZORPAY_KEY_SECRET')))
        razorpay_order = client.order.create(
            {"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1"}
        )
        order = Order.objects.create(
            name=name, amount=amount, provider_order_id=payment_order["id"]
        )
        order.save()
        return render(
            request,
            "razorpay.html",
            {
                "callback_url": "http://" + "127.0.0.1:8000" + "/razo  rpay/callback/",
                "razorpay_key": config('RAZORPAY_KEY_ID'),
                "order": order,
            },
        )
    return render(request, "razorpay.html.html")