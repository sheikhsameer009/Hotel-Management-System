from unicodedata import name
from django.urls import path

from . import views 

urlpatterns = [ 
    path('', views.index, name='index'),
    path('hotelweb/index', views.index, name='index'),
    path("hotelweb/", views.register, name='register'),
    path("hotelweb/register", views.register, name='register'),
    path("hotelweb/login", views.login, name='login'),
    path("hotelweb/guest_home", views.guest_home, name='guest_home'),
    path("hotelweb/booking", views.booking, name='booking'),
    path("hotelweb/roomservice", views.roomservice, name='roomservice'),
    path("hotelweb/payment", views.payment, name='payment'),
    path("hotelweb/rec_home", views.rec_home, name='rec_home'),
    path("hotelweb/booking_view/<int:booking_id>", views.booking_view, name='booking_view'),
    path("hotelweb/booking_update/<int:booking_id>", views.booking_update, name='booking_update')
]
