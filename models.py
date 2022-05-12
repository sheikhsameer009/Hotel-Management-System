# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Booking(models.Model):
    booking_id = models.IntegerField(db_column='Booking_ID', primary_key=True)  # Field name made lowercase.
    guest = models.ForeignKey('Guest', models.DO_NOTHING, db_column='Guest_ID', blank=True, null=True)  # Field name made lowercase.
    room_no = models.ForeignKey('Room', models.DO_NOTHING, db_column='Room_no', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='Startdate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='Enddate', blank=True, null=True)  # Field name made lowercase.
    checkout = models.TimeField(db_column='Checkout', blank=True, null=True)  # Field name made lowercase.
    receptionist = models.ForeignKey('Receptionist', models.DO_NOTHING, db_column='Receptionist_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'booking'


class CallForService(models.Model):
    guest = models.OneToOneField('Guest', models.DO_NOTHING, db_column='Guest_ID', primary_key=True)  # Field name made lowercase.
    room_service = models.ForeignKey('RoomService', models.DO_NOTHING, db_column='Room_Service_ID')  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    time = models.TimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'call_for_service'
        unique_together = (('guest', 'room_service'),)


class Chef(models.Model):
    id = models.OneToOneField('Employee', models.DO_NOTHING, db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chef'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employee(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=12, blank=True, null=True)  # Field name made lowercase.
    job_type = models.CharField(db_column='Job_Type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    salary = models.IntegerField(db_column='Salary', blank=True, null=True)  # Field name made lowercase.
    manager = models.ForeignKey('self', models.DO_NOTHING, db_column='Manager_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employee'


class Guest(models.Model):
    guest_id = models.IntegerField(db_column='Guest_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    email_address = models.CharField(db_column='Email_Address', max_length=35, blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nationality = models.CharField(db_column='Nationality', max_length=15, blank=True, null=True)  # Field name made lowercase.
    payment = models.ForeignKey('PaymentInfo', models.DO_NOTHING, db_column='Payment_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'guest'


class Menu(models.Model):
    item_id = models.IntegerField(db_column='Item_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=15, blank=True, null=True)  # Field name made lowercase.
    serving_persons = models.IntegerField(db_column='Serving_Persons', blank=True, null=True)  # Field name made lowercase.
    availability = models.IntegerField(db_column='Availability', blank=True, null=True)  # Field name made lowercase.
    cook = models.ForeignKey(Chef, models.DO_NOTHING, db_column='Cook_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'menu'


class OrderedItems(models.Model):
    order = models.OneToOneField('Orders', models.DO_NOTHING, db_column='Order_ID', primary_key=True)  # Field name made lowercase.
    item = models.ForeignKey(Menu, models.DO_NOTHING, db_column='Item_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ordered_items'
        unique_together = (('order', 'item'),)


class Orders(models.Model):
    order_id = models.IntegerField(db_column='Order_ID', primary_key=True)  # Field name made lowercase.
    guest = models.ForeignKey(Guest, models.DO_NOTHING, db_column='Guest_ID', blank=True, null=True)  # Field name made lowercase.
    menu_items = models.TextField(db_column='Menu_Items', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    time = models.TimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    bill = models.IntegerField(db_column='Bill', blank=True, null=True)  # Field name made lowercase.
    delivered_by = models.ForeignKey('RoomService', models.DO_NOTHING, db_column='Delivered_by', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders'


class PaymentInfo(models.Model):
    paymentid = models.IntegerField(db_column='Paymentid', primary_key=True)  # Field name made lowercase.
    card_no = models.CharField(db_column='Card_No', max_length=18)  # Field name made lowercase.
    cvv = models.IntegerField(db_column='CVV')  # Field name made lowercase.
    expiry = models.DateField(db_column='Expiry')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payment_info'


class ProvidesServices(models.Model):
    room_no = models.OneToOneField('Room', models.DO_NOTHING, db_column='Room_No', primary_key=True)  # Field name made lowercase.
    room_service = models.ForeignKey('RoomService', models.DO_NOTHING, db_column='Room_Service_ID')  # Field name made lowercase.
    shift = models.CharField(db_column='Shift', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'provides_services'
        unique_together = (('room_no', 'room_service'),)


class Receptionist(models.Model):
    id = models.OneToOneField(Employee, models.DO_NOTHING, db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'receptionist'


class Reservation(models.Model):
    reservation_id = models.IntegerField(db_column='Reservation_ID', primary_key=True)  # Field name made lowercase.
    guest = models.ForeignKey(Guest, models.DO_NOTHING, db_column='Guest_ID', blank=True, null=True)  # Field name made lowercase.
    table_no = models.ForeignKey('RestaurantTable', models.DO_NOTHING, db_column='Table_no', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    time = models.TimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    receptionist = models.ForeignKey(Receptionist, models.DO_NOTHING, db_column='Receptionist_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reservation'


class RestaurantTable(models.Model):
    table_no = models.IntegerField(db_column='Table_no', primary_key=True)  # Field name made lowercase.
    table_type = models.CharField(db_column='Table_Type', max_length=15, blank=True, null=True)  # Field name made lowercase.
    availability = models.IntegerField(db_column='Availability', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'restaurant_table'


class Room(models.Model):
    room_no = models.IntegerField(db_column='Room_no', primary_key=True)  # Field name made lowercase.
    room_type = models.CharField(db_column='Room_Type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rent = models.IntegerField(db_column='Rent', blank=True, null=True)  # Field name made lowercase.
    availability = models.IntegerField(db_column='Availability', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'room'


class RoomService(models.Model):
    id = models.OneToOneField(Employee, models.DO_NOTHING, db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'room_service'


class Serves(models.Model):
    waiter = models.OneToOneField('Waiter', models.DO_NOTHING, db_column='Waiter_ID', primary_key=True)  # Field name made lowercase.
    table_no = models.ForeignKey(RestaurantTable, models.DO_NOTHING, db_column='Table_No')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'serves'
        unique_together = (('waiter', 'table_no'),)


class Waiter(models.Model):
    id = models.OneToOneField(Employee, models.DO_NOTHING, db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'waiter'
