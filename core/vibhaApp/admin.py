from django.contrib import admin
from vibhaApp.models import *

# Register your models here.
class emailVerAdminModel(admin.ModelAdmin):
    list_display = ['isVerified','user_email','user_mobile']

class registerAdminModel(admin.ModelAdmin):
    list_display = ["primary_email","isEmailVerified","isPaid","designation","primary_mobile"]
    search_fields = ("primary_email","isEmailVerified","isPaid","designation","primary_mobile")

admin.site.register(Email_Verification,emailVerAdminModel)
admin.site.register(Registration,registerAdminModel)
admin.site.register(Order)
