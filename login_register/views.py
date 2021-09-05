from django.shortcuts import render
from .forms import *
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import *
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,DetailView,UpdateView
from django.urls import reverse,reverse_lazy
from django.db.models import Q 

from .date import datedata,month

from datetime import datetime, timedelta

# Create your views here.
def homeview(request):
    return render(request,'login_regi/home.html')




# def  RegisterForms(request):
#     registered = False
#     if request.method == 'POST':
#         form1 = Userform(request.POST)
#         form2 = profilepictures(request.POST)
#         if form1.is_valid() and form2.is_valid():
#             obj = form1.save()
#             obj.set_password(obj.password)
#             obj.save()

#             pro = form2.save()
#             pro.user = obj
#             if 'photo' in request.FILES:
#                 pro.photo = request.FILES['photo']
#                 pro.save()
#             registered = True
#             return redirect('home')

#     else:
#         form1 = Userform()
#         form2 = profilepictures()
#     context={
#         'form1':form1,
#         'form2':form2,
#         'reg':registered
        
#     }
#     return render(request,'login_regi/contact.html',context)

def  RegisterForms(request):

    registered = False
    if request.method == 'POST':
        user_form = Userform(data=request.POST)
        profile_form = profilepictures(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            obj = user_form.save()
            obj.set_password(obj.password)
            obj.save()
            profilepicturess = profile_form.save(commit=False)
            profilepicturess.user= obj
            if 'photo' in request.FILES:
                profilepicturess.photo = request.FILES['photo']
                profilepicturess.save()
                registered= True
            else:
                print('error')
            return redirect('login')
    else:
        user_form = Userform()
        profile_form = profilepictures()
       
    return render(request,'login_regi/contact.html',{
            'user_form':user_form,
            'profile_form':profile_form,
             'reg':registered,
        })





class ASn_POst(CreateView,LoginRequiredMixin):
    form_class = PostNews
    model = Post_Asn
    template_name = 'goninda/post.html'

class post_loc(CreateView,LoginRequiredMixin):
    form_class = locs
    model = location_model
    template_name = 'goninda/location.html'



class loc_list(LoginRequiredMixin,ListView):
    context_object_name = 'loc_list'
    model = location_model
    template_name= 'goninda/loc_list.html'
    queryset = location_model.objects.filter()





class ASn_POst_listview(LoginRequiredMixin,ListView):
    context_object_name = 'listdata'
    model = Post_Asn
    template_name= 'goninda/list.html'
    queryset = Post_Asn.objects.filter()



class postUpdate(LoginRequiredMixin, UpdateView):
    form_class = PostNews
    model = Post_Asn
    template_name = 'uplode_news.html'




class postUpdate_loc(LoginRequiredMixin, UpdateView):
    form_class = locs
    model = location_model
    template_name = 'goninda/loc_update.html'

class postdel_loc(LoginRequiredMixin, DeleteView):
    model = location_model
    template_name = 'goninda/loc_de.html'
    success_url = reverse_lazy('lsoc')

class postDelete(LoginRequiredMixin, DeleteView):
    model = Post_Asn
    template_name = 'delete_news.html'
    success_url = reverse_lazy('homes')




# class SearchResultsView(ListView):
#     model = Post_Asn
#     template_name = 'search_results.html'

#     def get_queryset(self): # new
#         query = self.request.GET.get('q')
#         object_list = Post_Asn.objects.filter(
#             Q(VLAN__icontains=query) | Q(LOCATION__icontains=query)
#         )
#         return object_list



from django.shortcuts import render
from django.db.models import Q


def SearchResultsView(request):
    if request.method == 'GET':
        query= request.GET.get('q')
        submitbutton= request.GET.get('submit')
        results= dailybilling.objects.filter(Q(date__icontains=query) | Q(cost_profile__cost_name__icontains=query))
        context={'results': results,
                     'submitbutton': submitbutton}
        return render(request, 'goninda/search_results.html', context)
    else:
        return render(request, 'goninda/search_results.html')




#   def get(self, request, category, *args, **kwargs):
#         authors = tag_createors.objects.filter(selet_channel__query_slug=category).values('tagSlug', 'tagNameBG','selet_channel__query_slug')
#         if authors:
#             posts = PostCreate.objects.filter(selete_channel_tag__query_slug=category).values('title', 'slug', 'photo','view','is_active','Seoimgalt').order_by('-id')
#             for author in list(authors):
#                 response = {
#                 'tagSlug': author['tagSlug'],
#                 'tagNameBG': author['tagNameBG'],
#                 'Main_Tag': author['selet_channel__query_slug']

#                 }
#             page = self.paginate_queryset(list(posts))
#             response['List'] = page
#             paginated_response = self.get_paginated_response(response)
#             return JsonResponse(paginated_response.data, safe=False)
#         return HttpResponse('No matching data found', status=404)



class post_user_data(LoginRequiredMixin,CreateView):
    form_class = userform
    model = userinfo
    template_name = 'nv/uplode_us.html'


class list_user(LoginRequiredMixin,ListView):
    context_object_name = 'list_user'
    model = userinfo
    template_name= 'nv/list_user.html'
    queryset = userinfo.objects.order_by('id')


class warning_user(LoginRequiredMixin,ListView):
    template_name= 'nv/warning_page.html'





def index(request):
    context = {
        'num_books': "This page only allowed super admin ('-')",
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'nv/warning_page.html', context=context)




 

def indexs(request):
    context = {
        'Pon_1': "Pon-1 : Tv center + Maijdee Bazar + AnswerCamp Rode",
        'Pon_2': "Pon-2 : Bothola + Rajgonj + Chodan",
        'Pon_3': "Pon-3 : Sonapur + Doterhat + Porobazar",
        'Pon_4': "Pon-4 : Lokkinaron Pur + Studiam Pichone + Master Para + Notun Bus stand +Napiterpoll ",
        'Pon_5': "Pon-5 : Soon",
        'Pon_6': "Pon-6 : Gabua",
        'Pon_7': "Pon-7 : Soon",
        'Pon_8': "Pon-8 : Soon",


 

    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'nv/pon_list.html', context=context)




def loc_lshotlist(request):
    context = {
        'LS': " LS - লক্ষীনারায়নপুর + সাতানী পুকুরপাড়",
        'GT': " GT - গাবুয়া + টিভি সেন্টার ",
        'RR': " RR - বটতলা + চড়ান + রাজগঞ্জ",
        'CR': " CR - নোয়াখালী পুরাতন কলেজ",
        'MB': " MB - মাইজদী বাজার",
        'HR': " HR - হাসপাতাল রোড ",
        'AC': " AC - আনসার ক্যাম্প রোড",
        'MP': " MP - মাস্টারপাড়া + নোয়াখালী নতুন কলেজ",
        'SP': " SP - শান্তি নাগার + পুলিশ লাইন রোড",
        'SD': " SD - সোনাপুর + দত্তেরহাট + পৌরবাজার",
        'HG': " HG - হাউজিং",
        'CC': " CC - Chorasta + Chawmuni",
        'NP': " NP - Notun Busstand + Napiter poll",


 


    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'nv/area.html', context=context)







# class post_user_dsata(LoginRequiredMixin,CreateView):
#     form_class = profilecostform
#     model = costprofile
#     template_name = 'nv/uplode_us.html'



# class posnt_user_dsata(LoginRequiredMixin,CreateView):
#     form_class = profilecostform
#     model = costprofile
#     template_name = 'nv/uplode_us.html'



class dailybing_view(LoginRequiredMixin,CreateView):

    form_class = dailyscosst
    model = dailybilling
    template_name = 'nv/uplode_us.html'






class daulycost_list(LoginRequiredMixin,ListView):


    context_object_name = 'fulllist'

    model = dailybilling
    template_name= 'goninda/list.html'
    #queryset = dailybilling.objects.filter(created_date__gte=datetime.now() - timedelta(days=1))
    # queryset = dailybilling.objects.filter(date__range=["202-08-11", "2021-09-11"]).exclude(cost_profile__cost_name__contains='Advance salary')
    queryset = dailybilling.objects.filter(date__range=datedata)


# class daulycost_list(LoginRequiredMixin,ListView):
#     context_object_name = 'fulllist'
#     model = dailybilling
#     template_name= 'goninda/list.html'
#     queryset = dailybilling.objects.filter(dateES__gt=datetime.now() - timedelta(hours=12))

class datashort_profile(LoginRequiredMixin,ListView):
    context_object_name = 'ssdxsx'
    model = dailybilling
    template_name= 'goninda/list.html'
    # queryset = dailybilling.objects.filter(cost_profile__contains='Terry')






class OFFICE_COST(LoginRequiredMixin,ListView):
    context_object_name = 'fulllist'
    model = dailybilling
    template_name= 'goninda/cost.html'
    queryset = dailybilling.objects.filter(cost_profile__cost_name__contains='Office Cost',date__range=datedata)



class OFFICE_bike(LoginRequiredMixin,ListView):
    context_object_name = 'fulllist'
    model = dailybilling
    template_name= 'goninda/cost.html'
    queryset = dailybilling.objects.filter(cost_profile__cost_name__contains='Bike Cost',date__range=datedata)



class OFFICE_family(LoginRequiredMixin,ListView):
    context_object_name = 'fulllist'
    model = dailybilling
    template_name= 'goninda/cost.html'
    queryset = dailybilling.objects.filter(cost_profile__cost_name__contains='Family',date__range=datedata)


class OFFICE_product(LoginRequiredMixin,ListView):
    context_object_name = 'fulllist'
    model = dailybilling
    template_name= 'goninda/cost.html'
    queryset = dailybilling.objects.filter(cost_profile__cost_name__contains='Product Cost',date__range=datedata)



class OFFICE_salllery(LoginRequiredMixin,ListView):
    context_object_name = 'fulllist'
    model = dailybilling
    template_name= 'goninda/cost.html'
    queryset = dailybilling.objects.filter(cost_profile__cost_name__contains='Salary',date__range=datedata)


class OFFICE_trnasportcost(LoginRequiredMixin,ListView):
    context_object_name = 'fulllist'
    model = dailybilling
    template_name= 'goninda/cost.html'
    queryset = dailybilling.objects.filter(cost_profile__cost_name__contains='Transport Cost',date__range=datedata)



class OFFICE_Chika(LoginRequiredMixin,ListView):
    context_object_name = 'fulllist'
    model = dailybilling
    template_name= 'goninda/cost.html'
    queryset = dailybilling.objects.filter(cost_profile__cost_name__contains='Chika',date__range=datedata)


class OFFICE_internetbill(LoginRequiredMixin,ListView):
    context_object_name = 'fulllist'
    model = dailybilling
    template_name= 'goninda/cost.html'
    queryset = dailybilling.objects.filter(cost_profile__cost_name__contains='orange',date__range=datedata)


class OFFICE_Electric(LoginRequiredMixin,ListView):
    context_object_name = 'fulllist'
    model = dailybilling
    template_name= 'goninda/cost.html'
    queryset = dailybilling.objects.filter(cost_profile__cost_name__contains='Electric Cost',date__range=datedata)



class OFFICE_Employ(LoginRequiredMixin,ListView):
    context_object_name = 'fulllist'
    model = dailybilling
    template_name= 'goninda/cost.html'
    queryset = dailybilling.objects.filter(cost_profile__cost_name__contains='Employ Cost',date__range=datedata)



class OFFICE_Pickup(LoginRequiredMixin,ListView):
    context_object_name = 'fulllist'
    model = dailybilling
    template_name= 'goninda/cost.html'
    queryset = dailybilling.objects.filter(cost_profile__cost_name__contains='Pickup Cost',date__range=datedata)




class updatedailyline(LoginRequiredMixin,ListView):
    context_object_name = 'fulllist'
    model = userupdate
    template_name= 'goninda/dalyconnection.html'





def updatessdata(request):
    allupdatedate = userupdate.objects.filter(date_user__range=["2021-08-11", "2021-09-11"])
    lastconnection = userupdate.objects.filter(date_user__range=["2021-08-11", "2021-09-11"]).last()
    totalsilveruser = userupdate.objects.filter(date_user__range=["2021-08-11", "2021-09-11"],pkg_namess__pkgname__startswith="Silver").count()
    totalgoldenuser = userupdate.objects.filter(date_user__range=["2021-08-11", "2021-09-11"],pkg_namess__pkgname__startswith="Gold").count()
    totalskyenuser = userupdate.objects.filter(date_user__range=["2021-08-11", "2021-09-11"],pkg_namess__pkgname__startswith="Sky").count()
    totaldaimondenuser = userupdate.objects.filter(date_user__range=["2021-08-11", "2021-09-11"],pkg_namess__pkgname__startswith="Daimond").count()
    totalstarenuser = userupdate.objects.filter(date_user__range=["2021-08-11", "2021-09-11"],pkg_namess__pkgname__startswith="Star").count()
    return render(request,"goninda/dalyconnection.html",{"dataone":allupdatedate,"datatwo":lastconnection,"usertype1":totalsilveruser,"usertype2":totalgoldenuser,"usertype3":totalskyenuser,"usertype4":totaldaimondenuser,"usertype5":totalstarenuser})






# class loosan(LoginRequiredMixin,ListView):
#     context_object_name = 'fulsllist'
#     model = loon
#     template_name= 'goninda/loon.html'




def looan(request):
    alldata = loon.objects.all()
    return render(request,"goninda/loon.html",{'alldata':alldata,})





# def montlybillview(request):
#     bill = monthlybill.objects.all()
#     paid_user = monthlybill.objects.filter(payment_status__name=True).count()
#     print(paid_user)
#     return render(request,"goninda/montlybill.html",{'bill':bill,'paidsuser':paid_user})

class montlybillview(LoginRequiredMixin,ListView):
    model = monthlybill
    template_name= 'goninda/montlybill.html'
    

    def get_context_data(self, **kwargs):
         context = super(montlybillview, self).get_context_data(**kwargs)
         context['alldata'] = monthlybill.objects.filter(month__month__startswith=month)
         context['totaluser'] = monthlybill.objects.filter(month__month__startswith=month).exclude(activities__act_line__startswith="declined").count()
         context['paiduser'] = monthlybill.objects.filter(payment_status=True,month__month__startswith=month).exclude(activities__act_line__startswith="declined").count()
         context['unpaiduser'] = monthlybill.objects.filter(payment_status=False,month__month__startswith=month).exclude(activities__act_line__startswith="declined").count()
         context['decline'] = monthlybill.objects.filter(activities__act_line__startswith="declined").count()

         context['selver'] = monthlybill.objects.filter(month__month__startswith=month,Pack_name__pkgnamebill__startswith="Selver").exclude(activities__act_line__startswith="declined").count()
         context['Gold'] = monthlybill.objects.filter(month__month__startswith=month,Pack_name__pkgnamebill__startswith="Gold").exclude(activities__act_line__startswith="declined").count()
         context['Diamond'] = monthlybill.objects.filter(month__month__startswith=month,Pack_name__pkgnamebill__startswith="Daimond").exclude(activities__act_line__startswith="declined").count()
         context['star'] = monthlybill.objects.filter(month__month__startswith=month,Pack_name__pkgnamebill__startswith="Star").exclude(activities__act_line__startswith="declined").count()
         context['sky'] = monthlybill.objects.filter(month__month__startswith=month,Pack_name__pkgnamebill__startswith="Sky").exclude(activities__act_line__startswith="declined").count()



         
         return context

        


from django.db.models import  Sum
class bkashpayment(ListView):
    model = monthlybill
    template_name= 'goninda/nk.html'

    def get_context_data(self, **kwargs):
         context = super(bkashpayment, self).get_context_data(**kwargs)
         context['ddfcdc'] = monthlybill.objects.filter(month__month__startswith=month).aggregate(Sum('pkg'))
         context['bkshuser'] = monthlybill.objects.filter(payment_method__methosd__contains='BKASH',month__month__startswith=month)
         context['countbkash'] = monthlybill.objects.filter(payment_method__methosd__contains='BKASH',month__month__startswith=month).count()
         context['countCASH'] = monthlybill.objects.filter(payment_method__methosd__contains='CASH',month__month__startswith=month).count()
         context['countNAGAD'] = monthlybill.objects.filter(payment_method__methosd__contains='NAGAD',month__month__startswith=month).count()
         context['totaluser'] = monthlybill.objects.all().count()
         context['paiduser'] = monthlybill.objects.filter(payment_status=True).count()
         context['unpaiduser'] = monthlybill.objects.filter(payment_status=False).count()
         return context
  

from django.db.models import  Sum

class nbox(ListView):
    model = monthlybill
    template_name= 'nbox/nk.html'

    def get_context_data(self, **kwargs):
         context = super(nbox, self).get_context_data(**kwargs)
         context['ddfcdc'] = monthlybill.objects.filter(month__month__startswith="July").aggregate(Sum('pkg'))
         context['bkshuser'] = monthlybill.objects.filter(payment_method__methosd__contains='BKASH',month__month__startswith="July")
         context['countbkash'] = monthlybill.objects.filter(payment_method__methosd__contains='BKASH',month__month__startswith="July").count()
         context['countCASH'] = monthlybill.objects.filter(payment_method__methosd__contains='CASH',month__month__startswith="July").count()
         context['countNAGAD'] = monthlybill.objects.filter(payment_method__methosd__contains='NAGAD',month__month__startswith="July").count()
         context['totaluser'] = monthlybill.objects.all().count()
         context['paiduser'] = monthlybill.objects.filter(payment_status=True).count()
         context['unpaiduser'] = monthlybill.objects.filter(payment_status=False).count()
         return context
  






# class bkashpayment(LoginRequiredMixin,ListView):
#     context_object_name = 'fulllist'
#     model = bkashuserpaymanet
#     template_name= 'goninda/nk.html'
  

# objects.filter(payment_method__methosd__contains='CASH').annotate(due_taka_total=Sum('duetaka__customer_due')).order_by('-customer_updated')
# class API_objedfcts(APIView, PaginationHandlerMixin):
#     pagination_class = StandadrdResultsSetPagination

#     def get(self, request, category, *args, **kwargs):
#         authors = tag_createors.objects.filter(tagSlug=category).values('tagSlug','tag_name')
#         if authors:
#             posts = PostCreate.objects.filter(tag_creator__tagSlug=category).values('title', 'slug', 'photo','release_date','view','SeoTitle','SeoMetaDes','Seoimgalt').order_by('-id')
#             for author in list(authors):
#                 response = {
#                 'tagSlug': author['tagSlug'],
#                 'tag_name': author['tag_name']

#                 }
#             page = self.paginate_queryset(list(posts))
#             response['List'] = page
#             paginated_response = self.get_paginated_response(response)
#             return JsonResponse(paginated_response.data, safe=False)
#         return HttpResponse('No matching data found', status=404)





def qurydata(request):
    if request.method == 'GET':
        query= request.GET.get('f')
        submitbutton= request.GET.get('subtmit')
        results= userupdate.objects.filter(Q(date_user__icontains=query))
        context={'results': results,
                     'submitbutton': submitbutton}
        return render(request, 'query/connectionnew.html', context)
    else:
        return render(request, 'query/connectionnew.html')



def dailyserach(request):
    if request.method == 'GET':
        query= request.GET.get('f')
        submitbutton= request.GET.get('subtmit')
        results= dailybilling.objects.filter(Q(date__icontains=query))
        context={'results': results,
                     'submitbutton': submitbutton}
        return render(request, 'query/daulynilingserach.html', context)
    else:
        return render(request, 'query/daulynilingserach.html')





class montlybill_update(LoginRequiredMixin, UpdateView):
    form_class = dailybillupdastefoms
    model = monthlybill
    template_name = 'goninda/loc_update.html'






class bkashtotal(LoginRequiredMixin,ListView):
    model = monthlybill
    template_name= 'goninda/bkashtotal.html'

    def get_context_data(self, **kwargs):
         context = super(bkashtotal, self).get_context_data(**kwargs)
         context['bkshuser'] =monthlybill.objects.filter(payment_method__methosd__contains='BKASH',month__month__startswith=month)
         context['selver1'] = monthlybill.objects.filter(payment_method__methosd__contains='BKASH',month__month__startswith=month,Pack_name__pkgnamebill__startswith="Selver").exclude(activities__act_line__startswith="declined").count()
         context['golden2'] = monthlybill.objects.filter(payment_method__methosd__contains='BKASH',month__month__startswith=month,Pack_name__pkgnamebill__startswith="Golden").exclude(activities__act_line__startswith="declined").count()
         context['daimond3'] = monthlybill.objects.filter(payment_method__methosd__contains='BKASH',month__month__startswith=month,Pack_name__pkgnamebill__startswith="Daimond").exclude(activities__act_line__startswith="declined").count()
         context['star4'] = monthlybill.objects.filter(payment_method__methosd__contains='BKASH',month__month__startswith=month,Pack_name__pkgnamebill__startswith="Star").exclude(activities__act_line__startswith="declined").count()
         context['sky5'] = monthlybill.objects.filter(payment_method__methosd__contains='BKASH',month__month__startswith=month,Pack_name__pkgnamebill__startswith="Sky").exclude(activities__act_line__startswith="declined").count()

         return context












class cash(LoginRequiredMixin,ListView):
    model = monthlybill
    template_name= 'goninda/cash.html'

    def get_context_data(self, **kwargs):
         context = super(cash, self).get_context_data(**kwargs)
         context['bkshuser'] = monthlybill.objects.filter(payment_method__methosd__contains='CASH',month__month__startswith=month)
         context['selver1'] = monthlybill.objects.filter(payment_method__methosd__contains='CASH',month__month__startswith=month,Pack_name__pkgnamebill__startswith="Selver").exclude(activities__act_line__startswith="declined").count()
         context['golden2'] = monthlybill.objects.filter(payment_method__methosd__contains='CASH',month__month__startswith=month,Pack_name__pkgnamebill__startswith="Golden").exclude(activities__act_line__startswith="declined").count()
         context['daimond3'] = monthlybill.objects.filter(payment_method__methosd__contains='CASH',month__month__startswith=month,Pack_name__pkgnamebill__startswith="Daimond").exclude(activities__act_line__startswith="declined").count()
         context['star4'] = monthlybill.objects.filter(payment_method__methosd__contains='CASH',month__month__startswith=month,Pack_name__pkgnamebill__startswith="Star").exclude(activities__act_line__startswith="declined").count()
         context['sky5'] = monthlybill.objects.filter(payment_method__methosd__contains='CASH',month__month__startswith=month,Pack_name__pkgnamebill__startswith="Sky").exclude(activities__act_line__startswith="declined").count()

         return context













#1
class cash_selver(LoginRequiredMixin,ListView):
    context_object_name = 'selver_cash'
    model = monthlybill
    template_name= 'pkg_data/selver.html'
    queryset = monthlybill.objects.filter(payment_method__methosd__contains='CASH',month__month__startswith=month,Pack_name__pkgnamebill__startswith="Selver").exclude(activities__act_line__startswith="declined")



#2
class golden_cash(LoginRequiredMixin,ListView):
    context_object_name = 'selver_cash'
    model = monthlybill
    template_name= 'pkg_data/golden.html'
    queryset = monthlybill.objects.filter(payment_method__methosd__contains='CASH',month__month__startswith=month,Pack_name__pkgnamebill__startswith="Gold").exclude(activities__act_line__startswith="declined")



#3
class Daimond_cash(LoginRequiredMixin,ListView):
    context_object_name = 'selver_cash'
    model = monthlybill
    template_name= 'pkg_data/daimond.html'
    queryset = monthlybill.objects.filter(payment_method__methosd__contains='CASH',month__month__startswith=month,Pack_name__pkgnamebill__startswith="Daimond").exclude(activities__act_line__startswith="declined")




#4
class selver_bk(LoginRequiredMixin,ListView):
    context_object_name = 'selver_cash'
    model = monthlybill
    template_name= 'pkg_data/bk/selverbk.html'
    queryset = monthlybill.objects.filter(payment_method__methosd__contains='BKASH',month__month__startswith=month,Pack_name__pkgnamebill__startswith="Selver").exclude(activities__act_line__startswith="declined")


#5
class goldenbk(LoginRequiredMixin,ListView):
    context_object_name = 'selver_cash'
    model = monthlybill
    template_name= 'pkg_data/bk/goldbk.html'
    queryset = monthlybill.objects.filter(payment_method__methosd__contains='BKASH',month__month__startswith=month,Pack_name__pkgnamebill__startswith="Gold").exclude(activities__act_line__startswith="declined")



class daimondbk(LoginRequiredMixin,ListView):
    context_object_name = 'selver_cash'
    model = monthlybill
    template_name= 'pkg_data/bk/daimondbk.html'
    queryset = monthlybill.objects.filter(payment_method__methosd__contains='BKASH',month__month__startswith=month,Pack_name__pkgnamebill__startswith="Daimond").exclude(activities__act_line__startswith="declined")
































class nagad(LoginRequiredMixin,ListView):
    context_object_name = 'bkshuser'
    model = monthlybill
    template_name= 'goninda/nagad.html'
    queryset = monthlybill.objects.filter(payment_method__methosd__contains='NAGAD',month__month__startswith=month)


class unpaid(LoginRequiredMixin,ListView):

    context_object_name = 'alldata'
    model = monthlybill
    template_name= 'goninda/montlybill.html'
    queryset =  monthlybill.objects.filter(payment_status=False,month__month__startswith=month).exclude(activities__act_line__startswith="declined")



class unpaidjuly(LoginRequiredMixin,ListView):
    context_object_name = 'alldata'
    model = monthlybill
    template_name= 'goninda/montlybill.html'
    queryset =  monthlybill.objects.filter(payment_status=False,month__month__startswith="July")


class unpaidAugust(LoginRequiredMixin,ListView):
    context_object_name = 'alldata'
    model = monthlybill
    template_name= 'goninda/montlybill.html'
    queryset =  monthlybill.objects.filter(payment_status=False,month__month__startswith="August").exclude(activities__act_line__startswith="declined")


class paydate(LoginRequiredMixin,ListView):
    model = monthlybill
    template_name= 'goninda/montlybill.html'

    def get_context_data(self, **kwargs):
         context = super(paydate, self).get_context_data(**kwargs)
         context['alldata'] = monthlybill.objects.filter(pay_date__range=["2021-05-09", "2021-05-11"])
         context['count'] = monthlybill.objects.filter(pay_date__range=["2021-05-09", "2021-05-11"]).count()
         return context
  




class adddmontlybill_front(LoginRequiredMixin,CreateView):

    form_class = dailybillupdastefoms
    model = monthlybill
    template_name = 'nv/uplode_monthbill.html'




class unpaidmay(LoginRequiredMixin,ListView):

    context_object_name = 'alldata'
    model = monthlybill
    template_name= 'goninda/montlybill.html'
    queryset =  monthlybill.objects.filter(payment_status=False).exclude(month__month__contains=month)






class routersell(LoginRequiredMixin,ListView):
    context_object_name = 'fulllist'
    model = router
    template_name= 'router.html'

def updateyssdata(request):
    alluyypsdatedate = router.objects.filter(date_user__range=["2021-08-11", "2021-09-11"])

    return render(request,"router.html",{"usertyyype5":alluyypsdatedate})






class routerpost(CreateView,LoginRequiredMixin):
    form_class = routerupdate
    model = router
    template_name = 'nv/uplode_router.html'




class loonpost(CreateView,LoginRequiredMixin):
    form_class = lodfdsfon
    model = loon
    template_name = 'nv/uplode_loon.html'



class dailyconnectionpost(CreateView,LoginRequiredMixin):
    form_class = dalyconnection
    model = userupdate
    template_name = 'nv/uplode_userupdate.html'




class uplode_srouter(CreateView,LoginRequiredMixin):
    form_class = srouters
    model = s_router
    template_name = 's_router/support.html'





class s_routerlist(LoginRequiredMixin,ListView):
    context_object_name = 'agglldata'
    model = s_router
    template_name= 's_router/list_srouter.html'
    queryset =  s_router.objects.filter(status=False)





class s_routerlist_update(LoginRequiredMixin, UpdateView):
    form_class = sroutssers
    model = s_router
    template_name = 's_router/update.html'




class s_routerlist(LoginRequiredMixin,ListView):
    context_object_name = 'agglldata'
    model = s_router
    template_name= 's_router/list_srouter.html'
    queryset =  s_router.objects.filter(status=False)




# class novus_employ(LoginRequiredMixin,ListView):
#     context_object_name = 'aggllssdata'
#     model = n_empoly
#     template_name= 's_router/userlist.html'

class iplist_block(LoginRequiredMixin,ListView):
    context_object_name = 'iplist'
    model = publicipnote
    template_name= 's_router/iplist.html'




class extra_in_view(LoginRequiredMixin,ListView):
    context_object_name = 'iplist'
    model = Extraincome
    template_name= 's_router/ex_lit.html'



class extra_in_viewcr(CreateView,LoginRequiredMixin):
    form_class = extra_in_form
    model = Extraincome
    template_name = 's_router/ex.html'




class Decline_user(LoginRequiredMixin,ListView):
    context_object_name = 'agglldata'
    model = monthlybill
    template_name= 's_router/declineuser.html'
    queryset =  monthlybill.objects.filter(payment_status=False,month__month__startswith=month,activities__act_line__startswith="declined" )