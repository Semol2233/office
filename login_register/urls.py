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
    path('areacode',loc_lshotlist,name='wssrn'),

    path('scsc',dailybing_view.as_view(),name='ijdfcdj'),
    path('',daulycost_list.as_view(),name='ijdfscdj'), 
    path('data',qurydata,name='datad'),
    path('srdaily',dailyserach,name='srdaily'),
    path('update/<int:pk>/',montlybill_update.as_view(),name='update'),




    path('office_cost',OFFICE_COST.as_view(),name='vddvd'),
    path('bike',OFFICE_bike.as_view(),name='bike'),
    path('family',OFFICE_family.as_view(),name='family'),
    path('product',OFFICE_product.as_view(),name='prdouct'),
    path('Salary',OFFICE_salllery.as_view(),name='Salary'),
    path('trnasportcost',OFFICE_trnasportcost.as_view(),name='trnasportcost'),
    path('Chika',OFFICE_Chika.as_view(),name='chika'),
    path('internetbill',OFFICE_internetbill.as_view(),name='internetbill'),
    path('Electric',OFFICE_Electric.as_view(),name='Electric'),
    path('Employ',OFFICE_Employ.as_view(),name='Employ'),
    path('Pickup',OFFICE_Pickup.as_view(),name='Pickup'),
    path('bkpayment',bkashpayment.as_view(),name='bkpayment'),
    path('update',updatedailyline.as_view(),name='updssate'),
    path('uspdate',updatessdata,name='update'),
    path('loon',looan,name='loon'),
    path('bill',montlybillview.as_view(),name='montslybillview'),
    path('bkash',bkashtotal.as_view(),name='bkashtotal'),

    path('cash',cash.as_view(),name='cash'),
    path('nagad',nagad.as_view(),name='nagad'),
    path('unpaid',unpaid.as_view(),name='unpaid'),

    path('9-10',paydate.as_view(),name='9to10'),

    path('add',adddmontlybill_front.as_view(),name='unpssaid'),
    path('mayunpaid',unpaidmay.as_view(),name='un'),
    path('sheet',nbox.as_view(),name='ung'),

    path('cash_selver',cash_selver.as_view(),name='selver_cash'),
    path('golden_selver',golden_cash.as_view(),name='golden_cash'),
    path('Daimond_cash',Daimond_cash.as_view(),name='Daimond_cash'),


    path('selver_bk',selver_bk.as_view(),name='selver_bk'),
    path('goldenbk',goldenbk.as_view(),name='goldenbk'),
    path('daimondbk',daimondbk.as_view(),name='daimondbk'),

    path('unpaidjuly',unpaidjuly.as_view(),name='dasimondbk'),
    path('Router',routersell.as_view(),name='daseimondbk'),

    path('postsouter',routerpost.as_view(),name='daseimossndddbk'),





    
    







 

]

