from django import forms
from django.contrib.auth.models import User
from .models import *


class Userform(forms.ModelForm):
    class Meta():
        model = User
        fields = ['username','password','email']
        widgets = {
          'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Namdde...'}),
          'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enddter Name...'}),
          'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Naddme...'}),
        }

class profilepictures(forms.ModelForm):
    class Meta():
        model = profileinfo
        fields = ['photo']



class PostNews(forms.ModelForm):
    class Meta:
        model = Post_Asn
        fields = ['id','VLAN','LOCATION','DESCRIPTION']
        widgets = {
            'VLAN':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name...'}),
            'LOCATION':forms.Select(attrs={'class':'form-control','placeholder':'Entdddder Name...'}),
            'DESCRIPTION':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Name...'})
          
        }
    def __init__(self,*args, **kwargs):
        super(PostNews,self).__init__(*args, **kwargs)
        self.fields['LOCATION'].empty_label="Location"


#dcnb

class locs(forms.ModelForm):
    class Meta:
        model = location_model
        fields = ['Location']
        widgets = {
            'Location':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name...'})
        }











class PostNewsup(forms.ModelForm):
    class Meta:
        model = Post_Asn
        fields = ['id','VLAN','LOCATION','DESCRIPTION']
        widgets = {
            'VLAN':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name...'}),
            'LOCATION':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name...'}),
            'DESCRIPTION':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Namdcdcde...'})
          
        }
        # def __init__(self,*args, **kwargs):
        #     super(Post_Asn,self).__init__(*args, **kwargs)
        #     self.fields['LOCATION'].empty_label="Select Author"


class DateInput(forms.DateInput):
    input_type = 'date'

class userform(forms.ModelForm):
    class Meta:
        model = userinfo
        fields = ['username','user_id','user_phone_number','package_name','user_onu_macaddr','payment','user_LOCATION','activition_date','pon_listf','user_addr']
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name...'}),
            'user_id':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name...'}),
            'user_phone_number':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name...'}),
            'package_name':forms.Select(attrs={'class':'form-control','placeholder':'Enter Name...'}),
            'user_addr':forms.Select(attrs={'class':'form-control','placeholder':'Enter Name...'}),
            'user_onu_macaddr':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name...'}),
            'payment':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Namdcdcde...'}),
            'user_LOCATION':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Namdcdcde...'}),
            'activition_date':DateInput(),
            'pon_listf':forms.Select(attrs={'class':'form-control','placeholder':'Enter Name...'}),

        }

    def __init__(self,*args, **kwargs):
        super(userform,self).__init__(*args, **kwargs)
        self.fields['pon_listf'].empty_label="Pon List"
        self.fields['package_name'].empty_label="package"
        self.fields['user_addr'].empty_label="Location"











class DateIsnput(forms.DateInput):
    input_type = 'date'

class dailyscosst(forms.ModelForm):
    class Meta:
        model = dailybilling
        fields = ['date','cost','description','cost_profile']
        widgets = {
            'date':DateIsnput(),
            'cost_profile':forms.Select(attrs={'class':'form-control','placeholder':'Offie Cost...'}),
            'cost':forms.TextInput(attrs={'class':'form-control','placeholder':'20tk....'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'office nasta..'})
        }

    def __init__(self,*args, **kwargs):
        super(dailyscosst,self).__init__(*args, **kwargs)
        self.fields['cost_profile'].empty_label="List"













class DateIsnput(forms.DateInput):
    input_type = 'date'

class dailybillupdatefoms(forms.ModelForm):
    class Meta:
        model = monthlybill
        fields = ['payment_method','pay_date','payment_status','pkg','description','month','user_id','activities','Pack_name']
        widgets = {
     
            'pay_date':DateIsnput(),
            'payment_method':forms.Select(attrs={'class':'form-control','placeholder':'Offie Cost.5555..'}),
            'pkg':forms.Select(attrs={'class':'form-control','placeholder':'Offie Cost.dfd55555..'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'.dfdf555555d.'}),
            'payment_status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),  
            'month': forms.Select(attrs={'class':'form-control'}), 
            'user_id': forms.TextInput(attrs={'class':'form-control'}),


        }

    def __init__(self,*args, **kwargs):
        super(dailybillupdatefoms,self).__init__(*args, **kwargs)
        self.fields['pkg'].empty_label="Selet Month"

    def __init__(self,*args, **kwargs):
        super(dailybillupdatefoms,self).__init__(*args, **kwargs)
        self.fields['month'].empty_label="Month"


    def __init__(self,*args, **kwargs):
        super(dailybillupdastefoms,self).__init__(*args, **kwargs)
        self.fields['activities'].empty_label="Connection Status"


    def __init__(self,*args, **kwargs):
        super(dailybillupdastefoms,self).__init__(*args, **kwargs)
        self.fields['Pack_name'].empty_label="Pkg Name"



class DateIssnput(forms.DateInput):
    input_type = 'date'

class dailybillupdastefoms(forms.ModelForm):
    class Meta:
        model = monthlybill
        fields = ['payment_method','pay_date','payment_status','activities','Pack_name','pkg','description','month','user_id']
        widgets = {
            
            'pay_date':DateIsnput(),
            'payment_method':forms.Select(attrs={'class':'form-control','placeholder':'Offie Cost...'}),
            'pkg':forms.Select(attrs={'class':'form-control','placeholder':'Offie Cost...'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'..'}),
            'payment_status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),  
            'month': forms.Select(attrs={'class':'form-control'}), 
            'user_id': forms.TextInput(attrs={'class':'form-control'}),
            'activities': forms.Select(attrs={'class':'form-control'}),
            'Pack_name': forms.Select(attrs={'class':'form-control'})



        }

    def __init__(self,*args, **kwargs):
        super(dailybillupdastefoms,self).__init__(*args, **kwargs)
        self.fields['pkg'].empty_label="Selet Month"

    def __init__(self,*args, **kwargs):
        super(dailybillupdastefoms,self).__init__(*args, **kwargs)
        self.fields['month'].empty_label="Month"

    def __init__(self,*args, **kwargs):
        super(dailybillupdastefoms,self).__init__(*args, **kwargs)
        self.fields['activities'].empty_label="Connection Status"


    def __init__(self,*args, **kwargs):
        super(dailybillupdastefoms,self).__init__(*args, **kwargs)
        self.fields['Pack_name'].empty_label="Pkg Name"






class DateIssnput(forms.DateInput):
    input_type = 'date'

class routerupdate(forms.ModelForm):
    class Meta:
        model = router
        fields = ['date_router','RounterBrand','Price','payment_methogd','Userid','description']
        widgets = {
            
            'date_router':DateIsnput(),
            'RounterBrand':forms.Select(attrs={'class':'form-control','placeholder':'Offie Cost...'}),
            'payment_methogd':forms.Select(attrs={'class':'form-control','placeholder':'Offie Cost...'}),
            'Price':forms.TextInput(attrs={'class':'form-control','placeholder':'..'}),
            'Userid':forms.TextInput(attrs={'class':'form-control','placeholder':'..'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'..'}),





        }

    def __init__(self,*args, **kwargs):
        super(routerupdate,self).__init__(*args, **kwargs)
        self.fields['RounterBrand'].empty_label="Router Brand"

  
    def __init__(self,*args, **kwargs):
        super(routerupdate,self).__init__(*args, **kwargs)
        self.fields['payment_methogd'].empty_label="Pay With" 






class lodfdsfon(forms.ModelForm):
    class Meta:
        model = loon
        fields = ['loon_date','loon_source','how_many','why_loon']
        widgets = {
            
            'loon_date':DateIsnput(),
            'loon_source':forms.Select(attrs={'class':'form-control','placeholder':'Offie Cost...'}),
            'why_loon':forms.Textarea(attrs={'class':'form-control','placeholder':'..'}),
            'how_many':forms.TextInput(attrs={'class':'form-control','placeholder':'..'}),


        }

    def __init__(self,*args, **kwargs):
        super(lodfdsfon,self).__init__(*args, **kwargs)
        self.fields['loon_source'].empty_label="Loon Source"




class dalyconnection(forms.ModelForm):
    class Meta:
        model = userupdate
        fields = ['date_user','user_sn','user_id','pkg_namess','user_name','prepaidbill','service_chagre','payment_method','auto_date']
        widgets = {
            
            'date_user':DateIsnput(),
            'user_sn':forms.TextInput(attrs={'class':'form-control','placeholder':'..'}),
            'user_id':forms.TextInput(attrs={'class':'form-control','placeholder':'..'}),
            'user_name':forms.TextInput(attrs={'class':'form-control','placeholder':'..'}),
            'prepaidbill':forms.TextInput(attrs={'class':'form-control','placeholder':'..'}),
            'service_chagre':forms.TextInput(attrs={'class':'form-control','placeholder':'..'}),
            'pkg_namess':forms.Select(attrs={'class':'form-control','placeholder':'Offie Cost...'}),
            'payment_method':forms.Select(attrs={'class':'form-control','placeholder':'Offie Cost...'}),
            'auto_date':forms.TextInput(attrs={'class':'form-control','placeholder':'..'}),

        }

    def __init__(self,*args, **kwargs):
        super(dalyconnection,self).__init__(*args, **kwargs)
        self.fields['pkg_namess'].empty_label="PKG"


    def __init__(self,*args, **kwargs):
        super(dalyconnection,self).__init__(*args, **kwargs)
        self.fields['payment_method'].empty_label="Pay With"





class srouters(forms.ModelForm):
    class Meta:
        model = s_router
        fields = ['date','userid','router_model','description','status']
        widgets = {
            
            'date':DateIsnput(),
            'userid':forms.TextInput(attrs={'class':'form-control','placeholder':'..'}),
            'router_model':forms.Select(attrs={'class':'form-control','placeholder':'Offie Cost...'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Offie Cost...'}),
            'status':forms.CheckboxInput(attrs={'class':'form-control','placeholder':'Offie Cost...'}),

          
        }

    def __init__(self,*args, **kwargs):
        super(srouters,self).__init__(*args, **kwargs)
        self.fields['router_model'].empty_label="Router Brand"



class sroutssers(forms.ModelForm):
    class Meta:
        model = s_router
        fields = ['status']
        widgets = {
            
           
            'status':forms.CheckboxInput(attrs={'class':'form-control','placeholder':'Offie Cost...'}),

          
        }




class extra_in_form(forms.ModelForm):
    class Meta:
        model = Extraincome
        fields = ['date','Source','Userid','Chrage','description','payment_methogd']
        widgets = {
            
            'date':DateIsnput(),
            'Userid':forms.TextInput(attrs={'class':'form-control','placeholder':'..'}),
            'Source':forms.Select(attrs={'class':'form-control','placeholder':'t...'}),
            'Chrage':forms.TextInput(attrs={'class':'form-control','placeholder':'..'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'...'}),
            'payment_methogd':forms.Select(attrs={'class':'form-control','placeholder':'Offie Cost...'}),

          
        }

