from django.db import models
from django.urls import reverse
# Create your models here.
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
import pytz
class profileinfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_pictures',blank=True)

    def __str__(self):
        return self.user.username




class location_model(models.Model):
    Location =  models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('lsoc')

    def __str__(self):
        return self.Location


class Post_Asn(models.Model):
    VLAN = models.IntegerField()
    DESCRIPTION = models.TextField()
    LOCATION = models.ForeignKey(location_model, on_delete=models.CASCADE ,blank=True, null=True ,related_name='books')
    
    def __str__(self):
        return self.VLAN

    def get_absolute_url(self):
        return reverse('homes')


















class package_list(models.Model):
    pk_name = models.CharField(max_length=255)
    def get_absolute_url(self):
        return reverse('lsoc')

    def __str__(self):
        return self.pk_name

class pon_list(models.Model):
    pon = models.CharField(max_length=255)
    def get_absolute_url(self):
        return reverse('lsoc')

    def __str__(self):
        return self.pon         

class user_loc(models.Model):
    user_loca = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('lsoc')

    def __str__(self):
        return self.user_loca


class userinfo(models.Model):
    username = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    user_addr = models.ForeignKey(user_loc, on_delete=models.CASCADE)
    user_phone_number = models.CharField(max_length=255)
    package_name  = models.ForeignKey(package_list, on_delete=models.CASCADE)
    pon_listf  = models.ForeignKey(pon_list, on_delete=models.CASCADE)
    user_onu_macaddr = models.CharField(max_length=255)
    payment = models.TextField()
    user_LOCATION = models.TextField()
    activition_date = models.DateTimeField()
    

    def get_absolute_url(self):
        return reverse('lsoc')

    def __str__(self):
        return self.username





class costprofile(models.Model):
    cost_name = models.CharField(max_length=255)
    def __str__(self):
        return self.cost_name

    def get_absolute_url(self):
        return reverse('lsoc')


class dailybilling(models.Model):
    date          = models.DateTimeField()
    cost_profile  = models.ForeignKey(costprofile, on_delete=models.CASCADE)
    cost          = models.CharField(max_length=255)
    description   = models.TextField()
    dateES         = models.DateTimeField(auto_now=True)
    created_date   = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('ijdfscdj')





class bkashuserpaymanet(models.Model):
    UserId = models.CharField(max_length=255)
    Ammount = models.CharField(max_length=255)

    def __str__(self):
        return self.UserId



class router_brnd(models.Model):
    router_brand = models.CharField(max_length=255)

    def __str__(self):
        return self.router_brand


class router(models.Model):
    date_router   =      models.DateTimeField()
    RounterBrand  =      models.ForeignKey(router_brnd, on_delete=models.CASCADE)
    Price         =      models.CharField(max_length=255)

    def __str__(self):
        return self.Price






class userupdate(models.Model):
    PAYMENT = (
        ('B', 'BKASH'),
        ('C', 'CASH'),
    )
    date_user =  models.DateTimeField()
    user_sn =  models.CharField(max_length=255,default=000)
    user_id = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    prepaidbill = models.CharField(max_length=255)
    service_chagre = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=1, choices=PAYMENT)
    auto_date =  models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user_name




class loon(models.Model):
    PAYMENT = (
        ('B', 'BKASH'),
        ('P', 'SERVICE CHRAGE'),
        ('M', 'MONTHLYBILL'),
        ('R', 'ROUTER')
    )
    loon_date = models.DateTimeField()
    loon_source     = models.CharField(max_length=1, choices=PAYMENT)
    how_many  =  models.CharField(max_length=255)
    why_loon  =  models.TextField()



    def __str__(self):
        return self.why_loon

class payment_methods(models.Model):
    methosd = models.CharField(max_length=255)
    
    def __str__(self):
        return self.methosd

class pkg(models.Model):
    pkg_list = models.CharField(max_length=255)
    
    def __str__(self):
        return self.pkg_list




class month_bill(models.Model):
    month = models.CharField(max_length=255)

    def __str__(self):
        return self.month


class monthlybill(models.Model):
    date             = models.DateTimeField(null=True, blank=True)
    activiton_date   = models.DateTimeField(null=True, blank=True)
    user_id          = models.CharField(max_length=255)
    user_phonenumber = models.CharField(max_length=255,blank=True)
    payment_method   = models.ForeignKey(payment_methods, on_delete=models.CASCADE)
    seletct_month   = models.ForeignKey(month_bill, on_delete=models.CASCADE)
    pay_date         = models.DateTimeField(null=True, blank=True)
    payment_status   = models.BooleanField(default=False)
    previus_due      = models.CharField(max_length=255,blank=True)
    pkg              = models.ForeignKey(pkg, on_delete=models.CASCADE)
    description      = models.TextField(blank=True)

    def __str__(self):
        return self.user_id


    def get_absolute_url(self):
        return reverse('montslybillview')

