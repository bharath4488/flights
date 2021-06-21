from django.contrib import admin
from django.urls import path, include
from Profile import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', views.login, name='login'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('home', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('archive', views.archive, name='archive'),
    path('about', views.about, name='about'),
    path('myflights', views.myflights, name='myflights'),
    path('profile', views.profile, name='profile'),
    path('flightshome', views.flightshome, name='flightshome'),
    path('flightshome/flightdetails', views.flightdetails, name='flightdetails'),
    path('flightshome/flightdetails/payments', views.payments, name='payments'),
   

    path('home/states', views.states.as_view(), name='states'),
    path('home/states/<slug:slug>', views.placesofinterest.as_view(), name='placesofinterest'),
    path('<int:pk>', views.poidetailview.as_view(), name='poidetailview'),


    path('garbage', views.garbage, name='garbage'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)