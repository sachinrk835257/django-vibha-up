from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from vibhaApp.models import Registration, Email_Verification ,Order
from django.conf import settings
# from vibhAuth import email_verify
from vibhaApp.email_otp import send_mail
from django.contrib import messages
from decouple import config
import uuid
import random
import json
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
        subject = '''VIBHA UP - Email Verification'''
        message = "Dear User,\n"
        html_message = f'<p>Email Verification -- OTP for verification is <strong> {otp} </strong>.</p>'
        send_mail(priEmail,subject,message, html_message)
        messages.add_message(request, messages.SUCCESS, "EMAIL SENT SUCCESSFULLY")

        register_obj = Registration.objects.create(accept_terms = terms,membership_fee = membership, dob = dob,district = selectCity, pin_code = pinCode, address = postAddress, state = selectState,country = countrySelect, interest = areaOfInterest, other_interest = otherInterest, full_name = name,institute_name = instituteName,designation =  designation, gender =gender, primary_email = priEmail, primary_mobile = priMobile,primary_whatsapp = priWhatsapp)

        register_obj.save()
        return redirect(f'http://127.0.0.1:8000/verify/{token}') 



    return render(request, 'vibhaApp/registration.html',{"title":title})

def contact(request):
    title = '''Vibha UP - Contact Us'''
    return render(request, 'vibhaApp/contact-us.html',{"title":title})


def verify_mail(request,token):
    # print("verification processing.....")
    title = '''Email Verification'''
    user_obj = Email_Verification.objects.filter(user_uuid=token).first()
    # print(user_obj)
    if request.method == "POST":
        fetch_otp = request.POST.get('otp')
        if user_obj.user_otp == fetch_otp:
            user_obj.isVerified = True
            register_obj = Registration.objects.get(primary_email = user_obj.user_email)
            # print(register_obj.isEmailVerified)
            register_obj.isEmailVerified = True
            user_obj.save()
            # print(register_obj.isEmailVerified)
            register_obj.save()
            messages.add_message(request, messages.SUCCESS, "Verification Done")
            return redirect(f'http://127.0.0.1:8000/payment/{register_obj.id}') 
            return HttpResponse("email verification done")
        else:        
            messages.add_message(request, messages.WARNING, "WRONG OTP!!")
            return redirect(f'http://127.0.0.1:8000/verify/{token}') 

    return render(request, 'vibhaAuth/email_otp.html',{"title":title,"email":user_obj.user_email})


def order_payment(request,id):
    title = '''Vibha UP - Pending Payment'''
    register_obj = Registration.objects.filter(id = id).first()
    print("in order_payment")
    if request.method == "POST":
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        payment_order_id = request.POST.get('payment_order_id')
        client = razorpay.Client(auth=(config('RAZORPAY_KEY_ID'), config('RAZORPAY_KEY_SECRET')))
        razorpay_order = client.order.create(
            {"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1"}
        )
        print("razorpay_order -- ",razorpay_order)
        order = Order.objects.create(
            name=name, email = email, phone_number = phone_number, amount=amount,provider_order_id=razorpay_order["id"]
        )
        order.save()
        return render(
            request,
            "vibhaApp/paymentstatus.html",
            {
                "callback_url": '''http://127.0.0.1:8000/razorpay/callback/''',
                "razorpay_key": config('RAZORPAY_KEY_ID'),
                "order": order,
            },
        )
    return render(request, 'vibhaApp/razorpay.html', {"title":title,"user":register_obj,"amount":1000})

@csrf_exempt
def callback(request):
    print("fdfffffffffffff", request.POST)
    def verify_signature(response_data):
        print("verify_signature",response_data["razorpay_payment_id"])
        client = razorpay.Client(auth=(config('RAZORPAY_KEY_ID'), config('RAZORPAY_KEY_SECRET')))
        print("status ---- ",client.utility.verify_payment_signature(response_data))
        return client.utility.verify_payment_signature(response_data)
    
    print("hhg")
    print("razorpay_signature" in request.POST)
    if "razorpay_signature" in request.POST: 
        # print("options -- ",request.POST)
        payment_id = request.POST.get("razorpay_payment_id", "")
        provider_order_id = request.POST.get("razorpay_order_id", "")
        signature_id = request.POST.get("razorpay_signature", "")
        print("4645646")
        order = Order.objects.get(provider_order_id=provider_order_id)
        user = Registration.objects.filter(primary_email=order.email).first()
        print("user",user)
        order.payment_id = payment_id
        order.signature_id = signature_id
        order.save()
        print("9896")
        if verify_signature(request.POST):
            order.status = 'SUCCESS' 
            order.save()
            print("64654")
            user.isPaid = True
            user.save()
            subject = '''VIBHA UP - Payment Succesfull'''
            message = "Dear User,\n"
            html_message = f'<p>You have done payment .<br>Your <strong> payment id -- {order.payment_id} </strong>.</p>'
            send_mail(user.primary_email,subject,message, html_message)
            print("email gone")

            # return HttpResponse(f"{order.status}")
            return render(request, "vibhaApp/paymentstatus.html", context={"status": order.status})
        else:
            print("54554")
            order.status = 'FAILURE'
            order.save()
            # return HttpResponse(f"{order.status}")
            return render(request, "vibhaApp/paymentstatus.html", context={"status": order.status})
    else:
        print("else request -- ",request.POST)
        payment_id = json.loads(request.POST.get("error[metadata]")).get("payment_id")
        provider_order_id = json.loads(request.POST.get("error[metadata]")).get(
            "order_id"
        )
        order = Order.objects.get(provider_order_id=provider_order_id)
        order.payment_id = payment_id
        order.status = 'FAILURE'
        order.save()
        # return HttpResponse(f"outside else {order.status}")
        return render(request, "vibhaApp/paymentstatus.html", context={"status": order.status})
