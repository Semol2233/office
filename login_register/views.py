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

        results= Post_Asn.objects.filter(Q(VLAN__icontains=query) | Q(LOCATION__Location__icontains=query) | Q(DESCRIPTION__icontains=query))

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



class post_user_data(CreateView,LoginRequiredMixin):
    form_class = userform
    model = userinfo
    template_name = 'nv/uplode_us.html'


class list_user(LoginRequiredMixin,ListView):
    context_object_name = 'list_user'
    model = userinfo
    template_name= 'nv/list_user.html'
    queryset = userinfo.objects.filter()


class warning_user(LoginRequiredMixin,ListView):
    template_name= 'nv/warning_page.html'





def index(request):
    context = {
        'num_books': "This page only allowed super admin ('-')",
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'nv/warning_page.html', context=context)