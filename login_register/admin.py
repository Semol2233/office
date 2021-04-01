from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.auth.models import  Group
admin.site.site_header = "Vlan Management"

admin.site.unregister(Group)
admin.site.register(package_list)
admin.site.register(pon_list)
admin.site.register(user_loc)
admin.site.register(userinfo)
admin.site.register(costprofile)
admin.site.register(dailybilling)
admin.site.register(bkashuserpaymanet)


