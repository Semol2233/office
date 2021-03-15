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


