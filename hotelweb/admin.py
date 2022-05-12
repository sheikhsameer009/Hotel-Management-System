from django.contrib import admin
from .models import Employee,Guest, PaymentInfo, ProvidesServices,Room,Booking, RoomService,User,CallForService

admin.site.register(Employee)
admin.site.register(Guest)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(User)
admin.site.register(PaymentInfo)
admin.site.register(RoomService)
admin.site.register(ProvidesServices)
admin.site.register(CallForService)
