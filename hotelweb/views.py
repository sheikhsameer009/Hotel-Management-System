from asyncio.windows_events import NULL
import email
from pickle import FALSE, TRUE
from subprocess import check_output
from tkinter.tix import Select
from django.db import connection
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login as auth_login ,authenticate,logout
import datetime

from hotelweb.models import Employee,Guest,User,Room,Booking,PaymentInfo,ProvidesServices,CallForService,RoomService
# Create your views here.

def index(request): 
    return render(request,'index.html') 

def register(request):
    msg=''
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        id = request.POST['id']
        email = request.POST['email']
        contact = request.POST['contact']
        nationality = request.POST['nationality']
        username = request.POST['username']
        password = request.POST['pass']
        password1 = request.POST['pass1']
        if password==password1:
            new_guest = Guest(guest_id=id,fname=fname,lname=lname,email_address=email,contact=contact,nationality=nationality)
            new_guest.save() 
            new_user = User.objects.create_user(username=username,password=password,email=email,first_name=fname,last_name=lname)
            new_user.save()
            return redirect('login')
        else:
            msg = 'Password is not matching'          

    return render(request,'register.html',{'msg':msg})

def login(request):
    msg = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None and user.is_guest:
            auth_login(request, user)
            return redirect('guest_home')
        elif user is not None and user.is_receptionist:
            auth_login(request,user)
            return redirect('rec_home')
        elif user is not None and user.is_admin:
            auth_login(request,user)
            return redirect('/admin')        
        else:
            msg='Invalid Credentials'    

    return render(request,'login.html',{'msg':msg})

def logout(request):
    logout(request)
    return render(request,'index.html')  

def guest_home(request): 
    return render(request,'guest_home.html')

def booking(request):
    if request.method == 'POST':
        startdate = request.POST['startdate']
        enddate = request.POST['enddate']
        room_no = request.POST['room']
        room = Room.objects.get(room_no=room_no)
        room.availability = False
        user_email = request.user.email
        print(user_email)
        guest = Guest.objects.get(email_address = user_email)
        new_booking = Booking.objects.create(startdate=startdate,enddate=enddate,room_no=room,guest_id = guest)
        new_booking.save()
        room.save()
        return redirect('payment')

    return render(request,'booking.html', {'rooms':Room.objects.filter(availability=True)})

def payment(request):
    if request.method == 'POST':
        card_no = request.POST['cn']
        cvc = request.POST['cvc']
        expiry = request.POST['expiry']
        new_payment = PaymentInfo.objects.create(card_no=card_no, cvv=cvc, expiry=expiry)
        new_payment.save()
        payment_id = PaymentInfo.objects.get(card_no=card_no)
        user_email = request.user.email
        guest_data = get_object_or_404(Guest,email_address=user_email)
        guest_data.payment_id = payment_id
        guest_data.save()
        return redirect('guest_home')
    return render(request, 'payment.html')

def rec_home(request):
    bookings = Booking.objects.filter(checkout__isnull = True)
    return render(request,'rec_home.html',{'bookings':bookings})

def booking_view(request,booking_id):
    booking = Booking.objects.get(booking_id = booking_id)
    return render(request,'booking_view.html',{'booking':booking})       

def booking_update(request,booking_id):
    if request.method =='POST':
        checkout = request.POST['checkout']
        user_email = request.user.email
        receptionist = Employee.objects.get(email_address = user_email)
        booking_data = get_object_or_404(Booking,booking_id=booking_id)
        booking_data.checkout = checkout
        booking_data.receptionist_id = receptionist.id
        booking_data.save()
        return redirect('rec_home')

    booking = Booking.objects.get(booking_id = booking_id)
    return render(request,'booking_update.html',{'booking':booking})     

def roomservice(request):
    if request.method =='POST':
        user_email = request.user.email
        guest_id = Guest.objects.get(email_address=user_email)
        booking_id = Booking.objects.get(guest_id=guest_id)
        room_no = booking_id.room_no
        currentdate = datetime.date.today()
        currenttime = datetime.datetime.now().time()
        room = ProvidesServices.objects.get(room_no=room_no)
        room_service = room.room_service_id
        new_service = CallForService.objects.create(guest_id=guest_id,date=currentdate,time=currenttime,room_service_id=room_service)
        new_service.save()
        return redirect('guest_home')
        

    return render(request,'roomservice.html')     