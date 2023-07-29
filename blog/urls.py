from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as bv

urlpatterns = [
    path('', bv.home, name="blog-home"),
    path('about/', bv.about, name="blog-about"),
    path('contact_us/', bv.contact_us, name="blog-contact_us"),
    path('our_mission/', bv.mission, name="blog-mission"),
    path('register/', bv.signup, name="blog-volunteer_signup"),
    path('registered', bv.register, name="blog-volunteer_register"),
    path('request', bv.req, name="blog-request"),
    path('requested', bv.requested, name="blog-requested"),
    path('check_status', bv.check_status, name="blog-check_status"),
    path('status', bv.status, name="blog-status"),
    path('requestlist', bv.requestlist, name="blog-requestlist"),
    path('food_bank_register', bv.foodbank, name="blog-food_bank_register"),
    path('food_bank/', bv.food_bank, name="blog-food_bank"),
    path('generate_report/', bv.volunteer_report, name="blog-vol_report"),
    path('volunteerreport/', bv.volreport, name="blog-volreport"),
    path('check_report/', bv.vrs, name="blog-vrs"),
    path('report/', bv.vr, name="blog-vr"),
    path('onsite_processing/', bv.onsite, name="blog-onsite"),
    path('os_process/', bv.os_processing, name="blog-osp"),
    path('donation_process/', bv.donation, name="blog-dp"),
    path('donationprocess/', bv.don_process, name="blog-donp"),
    path('accept/', bv.accept, name="blog-accept"),
    path('profile/', bv.profile, name="blog-profile"),
    path('login/', bv.login, name="blog-login"),
    path('loggedin/', bv.loggedin, name="blog-loggedin"),
    path('logout/', bv.loggedout, name="blog-logout"),
    path('change_password/', bv.change_password, name="blog-change"),
    path('changed_password/', bv.changed_password, name="blog-password")
]

handler404 = bv.handler404
