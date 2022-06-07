from django.urls import path
from . import views
urlpatterns=[
    path('',views.homepage),
    path('registerpage',views.registerpage),
    path('saving_form_data',views.saving_form_data),
    path('loginpage',views.loginpage),
    path('check_login',views.check_login),
    path('user_logout',views.user_logout),
    path('search_donor',views.search_donor),
    path('requesting',views.requesting),
    path('accept_request',views.accept_request),
    path('reject_request',views.reject_request),
    path('approve_donors',views.approve_donors),
    path('approve',views.approve),
    path('admin_logout',views.admin_logout),
    path('update_profile',views.update_profile),
    path('updation',views.updation)

]