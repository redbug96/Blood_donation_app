from django.contrib import admin

# Register your models here.
from app1.models import Donor,Login,Request_donor
admin.site.register(Donor)
admin.site.register(Login)
admin.site.register(Request_donor)