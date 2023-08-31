from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Email_Verification(models.Model):
    user_email = models.EmailField(default="")
    user_mobile = models.CharField(max_length=10,default="")
    user_uuid = models.CharField(max_length=255, default="")
    user_otp = models.CharField(max_length=4,default="")
    isVerified = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user_email
    

class Registration(models.Model):
    primary_email = models.EmailField(default="",blank=False,null=False)
    primary_whatsapp = models.CharField(default="", max_length=10)
    primary_mobile = models.CharField(default="", max_length=10,unique=True,blank=False,null=False)
    gender = models.CharField(default="Male", max_length=6)
    designation = models.CharField(default="", max_length=10)
    full_name = models.CharField(default="", max_length=52)
    institute_name = models.CharField(default="", max_length=100)
    interest = models.CharField(default="", max_length=20)
    other_interest = models.CharField(max_length=50,default="Null")
    country = models.CharField(default="", max_length=10)
    state = models.CharField(default="", max_length=20)
    district = models.CharField(default="",max_length=80)
    address = models.CharField(default="",max_length=80)
    pin_code = models.CharField(default="",max_length=6)
    district = models.CharField(default="",max_length=80)
    dob = models.DateField(default="")
    membership_fee = models.CharField(max_length=30,default="1000 individual")
    accept_terms = models.CharField(default="False",max_length=20)

    isEmailVerified = models.BooleanField(default=False)
    isPaid = models.BooleanField(default=False)

    def __str__(self):
        return self.primary_email
    

class Order(models.Model):
    name = models.CharField(_("Customer Name"), max_length=254, blank=False, null=False)
    email = models.EmailField(_("Customer Email"), max_length=254, blank=False, null=False) #should be unique
    phone_number = models.CharField(_("Customer Phone Number"), max_length=10, blank=False, null=False)    #should be unique
    amount = models.FloatField(_("Amount"), null=False, blank=False)
    status = models.CharField(
        _("Payment Status"),
        default= 'PENDING',
        max_length=254,
        blank=False,
        null=False,
    )
    provider_order_id = models.CharField(
        _("Order ID"), max_length=40, null=False, blank=False
    )
    payment_id = models.CharField(
        _("Payment ID"), max_length=36, null=False, blank=False
    )
    signature_id = models.CharField(
        _("Signature ID"), max_length=128, null=False, blank=False
    )

    def __str__(self):
        return f"{self.id}-{self.email}-{self.name}-{self.status}"
