from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.auth.models import  Group
admin.site.site_header = "Vlan Management"

admin.site.unregister(Group)
# admin.site.register(package_list)
# admin.site.register(pon_list)
# admin.site.register(user_loc)
# admin.site.register(userinfo)
admin.site.register(costprofile)
admin.site.register(dailybilling)
admin.site.register(bkashuserpaymanet)
admin.site.register(router_brnd)
admin.site.register(router)
admin.site.register(userupdate)
admin.site.register(loon)
admin.site.register(monthlybill)
admin.site.register(payment_methods)
admin.site.register(pkg)
admin.site.register(month_bill)
admin.site.register(pkg_names)
admin.site.register(actrline)
admin.site.register(pkg_namesbill)
admin.site.register(router_payment)
admin.site.register(loonsource)
admin.site.register(s_router)
admin.site.register(publicipnote)


























