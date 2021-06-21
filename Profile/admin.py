from django.contrib import admin
from .models import userprofile, Airport, User_querie, flightbookingshistory, state, Points_of_Interest


# Register your models here.
admin.site.register(userprofile)
admin.site.register(Airport)
admin.site.register(User_querie)
admin.site.register(flightbookingshistory)
admin.site.register(state)

class POIadmin(admin.ModelAdmin):
  list_display = ('Point_of_interest','State_name','city','category')
admin.site.register(Points_of_Interest, POIadmin)
