from django.contrib import admin
from django.contrib.auth.models import User

from diningdeck.models import Restaurant, UserEaten
# Register your models here.


#class UserInline(admin.TabularInline):
#    model = User

class RestaurantAdmin(admin.ModelAdmin):
    search_fields = ['restaurant']


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(UserEaten)