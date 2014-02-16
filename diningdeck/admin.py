from django.contrib import admin
from diningdeck.models import Restaurant, User
# Register your models here.


class UserInline(admin.TabularInline):
    model = User

class RestaurantAdmin(admin.ModelAdmin):
    search_fields = ['restaurant']


admin.site.register(Restaurant, RestaurantAdmin)
