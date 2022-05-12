from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here
from django.db import models

class Employee(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fname = models.CharField(db_column='FName', max_length=45)  # Field name made lowercase.
    lname = models.CharField(db_column='LName', max_length=25)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)  # Field name made lowercase.
    email_address = models.CharField(db_column='Email_Address', max_length=35, blank=True, null=True)
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=12, blank=True, null=True)  # Field name made lowercase.
    job_type = models.CharField(db_column='Job_Type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    salary = models.IntegerField(db_column='Salary', blank=True, null=True)  # Field name made lowercase.
    manager = models.ForeignKey('self', models.DO_NOTHING, db_column='Manager_ID', blank=True, null=True)  # Field name made lowercase.

    def __int__(self):
        return self.id
    
    class Meta:
        managed = True
        db_table = 'employee'

class Chef(models.Model):
    id = models.OneToOneField('Employee', models.DO_NOTHING, db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'chef'
        
class Receptionist(models.Model):
    id = models.OneToOneField(Employee, models.DO_NOTHING, db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'receptionist'

class RoomService(models.Model):
    id = models.OneToOneField(Employee, models.DO_NOTHING, db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'room_service'

class Waiter(models.Model):
    id = models.OneToOneField(Employee, models.DO_NOTHING, db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'waiter'

class PaymentInfo(models.Model):
    paymentid = models.AutoField(db_column='Paymentid', primary_key=True)  # Field name made lowercase.
    card_no = models.CharField(db_column='Card_No', max_length=19)  # Field name made lowercase.
    cvv = models.IntegerField(db_column='CVV')  # Field name made lowercase.
    expiry = models.DateField(db_column='Expiry')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'payment_info'

class Guest(models.Model):
    guest_id = models.IntegerField(db_column='Guest_ID', primary_key=True)  # Field name made lowercase.
    fname = models.CharField(db_column='FName', max_length=45)  # Field name made lowercase.
    lname = models.CharField(db_column='LName', max_length=45)  # Field name made lowercase.
    email_address = models.CharField(db_column='Email_Address', max_length=35, blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nationality = models.CharField(db_column='Nationality', max_length=15, blank=True, null=True)  # Field name made lowercase.
    payment = models.ForeignKey('PaymentInfo', models.DO_NOTHING, db_column='Payment_ID', blank=True, null=True)  # Field name made lowercase.

    def __int__(self):
        return self.guest_id

    def __str__(self):
        return self.fname
    

    class Meta:
        managed = True
        db_table = 'guest'

class Room(models.Model):
    room_no = models.IntegerField(db_column='Room_no', primary_key=True)  # Field name made lowercase.
    room_type = models.CharField(db_column='Room_Type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rent = models.IntegerField(db_column='Rent', blank=True, null=True)  # Field name made lowercase.
    availability = models.BooleanField(db_column='Availability', default=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.room_no)
    
    class Meta:
        managed = True
        db_table = 'room'

class RestaurantTable(models.Model):
    table_no = models.IntegerField(db_column='Table_no', primary_key=True)  # Field name made lowercase.
    table_type = models.CharField(db_column='Table_Type', max_length=15, blank=True, null=True)  # Field name made lowercase.
    availability = models.BooleanField(db_column='Availability', default=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'restaurant_table'        

class Menu(models.Model):
    item_id = models.AutoField(db_column='Item_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=15, blank=True, null=True)  # Field name made lowercase.
    serving_persons = models.IntegerField(db_column='Serving_Persons', blank=True, null=True)  # Field name made lowercase.
    availability = models.BooleanField(db_column='Availability', default=True)  # Field name made lowercase.
    cook = models.ForeignKey(Chef, models.DO_NOTHING, db_column='Cook_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'menu'

class Booking(models.Model):
    booking_id = models.AutoField(db_column='Booking_ID', primary_key=True)  # Field name made lowercase.
    guest = models.ForeignKey('Guest', models.DO_NOTHING, db_column='Guest_ID', blank=True, null=True)  # Field name made lowercase.
    room_no = models.ForeignKey('Room', models.DO_NOTHING, db_column='Room_no', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='Startdate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='Enddate', blank=True, null=True)  # Field name made lowercase.
    checkout = models.TimeField(db_column='Checkout', blank=True, null=True)  # Field name made lowercase.
    receptionist = models.ForeignKey('Receptionist', models.DO_NOTHING, db_column='Receptionist_ID', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.booking_id)
    
    class Meta:
        managed = True
        db_table = 'booking'

class Reservation(models.Model):
    reservation_id = models.AutoField(db_column='Reservation_ID', primary_key=True)  # Field name made lowercase.
    guest = models.ForeignKey(Guest, models.DO_NOTHING, db_column='Guest_ID', blank=True, null=True)  # Field name made lowercase.
    table_no = models.ForeignKey('RestaurantTable', models.DO_NOTHING, db_column='Table_no', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    time = models.TimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    receptionist = models.ForeignKey(Receptionist, models.DO_NOTHING, db_column='Receptionist_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reservation'        

class Orders(models.Model):
    order_id = models.AutoField(db_column='Order_ID', primary_key=True)  # Field name made lowercase.
    guest = models.ForeignKey(Guest, models.DO_NOTHING, db_column='Guest_ID', blank=True, null=True)  # Field name made lowercase.
    menu_items = models.TextField(db_column='Menu_Items', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    time = models.TimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    bill = models.IntegerField(db_column='Bill', blank=True, null=True)  # Field name made lowercase.
    delivered_by = models.ForeignKey('RoomService', models.DO_NOTHING, db_column='Delivered_by', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'orders'

class CallForService(models.Model):
    guest = models.OneToOneField('Guest', models.DO_NOTHING, db_column='Guest_ID', primary_key=True)  # Field name made lowercase.
    room_service = models.ForeignKey('RoomService', models.DO_NOTHING, db_column='Room_Service_ID')  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    time = models.TimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'call_for_service'
        unique_together = (('guest', 'room_service'),)


class OrderedItems(models.Model):
    order = models.OneToOneField('Orders', models.DO_NOTHING, db_column='Order_ID', primary_key=True)  # Field name made lowercase.
    item = models.ForeignKey(Menu, models.DO_NOTHING, db_column='Item_ID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ordered_items'
        unique_together = (('order', 'item'),)

class ProvidesServices(models.Model):
    room_no = models.OneToOneField('Room', models.DO_NOTHING, db_column='Room_No', primary_key=True)  # Field name made lowercase.
    room_service = models.ForeignKey('RoomService', models.DO_NOTHING, db_column='Room_Service_ID')  # Field name made lowercase.
    shift = models.CharField(db_column='Shift', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'provides_services'
        unique_together = (('room_no', 'room_service'),)

class Serves(models.Model):
    waiter = models.OneToOneField('Waiter', models.DO_NOTHING, db_column='Waiter_ID', primary_key=True)  # Field name made lowercase.
    table_no = models.ForeignKey(RestaurantTable, models.DO_NOTHING, db_column='Table_No')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'serves'
        unique_together = (('waiter', 'table_no'),)          


class User(AbstractUser):
    is_admin = models.BooleanField('isadmin',default=False)
    is_receptionist = models.BooleanField('isreceptionist',default=False)
    is_owner = models.BooleanField('isowner',default=False)
    is_guest = models.BooleanField('isguest',default=True)
