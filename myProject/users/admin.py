from django.contrib import admin
from .models import Profile

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','image', 'firstname', 'lastname', 'dob', 'phone', 'address',
                   'city', 'country', 'zipCode',)
admin.site.register(Profile,ProfileAdmin)





