from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import  Group
admin.site.site_header = "Vlan Management"

admin.site.unregister(Group)
