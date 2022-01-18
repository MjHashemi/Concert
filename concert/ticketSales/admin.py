from django.contrib import admin
from ticketSales.models import concertModel,locationModel,timeModel,ticketModel

# Register your models here.

admin.site.register(concertModel)
admin.site.register(locationModel)
admin.site.register(timeModel)
admin.site.register(ticketModel)
