from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('fggvf',homeview,name='home'),
    path('form/',RegisterForms,name='hoggme'),
    path('fv',ASn_POst.as_view(),name='homssses'),
    path('sxs',ASn_POst_listview.as_view(),name='homes'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('up/<int:pk>/',postUpdate.as_view(),name='up'),
    path('del/<int:pk>/',postDelete.as_view(),name='del'),
    path('se/',SearchResultsView,name='serach'),
    path('loc/',post_loc.as_view(),name='loc'),
    path('loc_list/',loc_list.as_view(),name='lsoc'),
    path('loc/<int:pk>/',postUpdate_loc.as_view(),name='lsoc_up'),
    path('loc_del/<int:pk>/',postdel_loc.as_view(),name='lsoc_del'),
    path('post_user_data',post_user_data.as_view(),name='user'),
    path('dd',list_user.as_view(),name='userlist'),
    path('shudf',warning_user.as_view(),name='wrs'),
    path('wr',index,name='wrn'),
    path('ponlist',indexs,name='wsrn'),
    path('scsc',dailybing_view.as_view(),name='ijdfcdj'),
    path('',daulycost_list.as_view(),name='ijdfscdj')




]