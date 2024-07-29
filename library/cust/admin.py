from django.contrib import admin
from cust.models import customer



@admin.register(customer)
class customerAdmin(admin.ModelAdmin):
    list_display= ['user','created_at','name', 'mobile','email', 'address', 'gender']

