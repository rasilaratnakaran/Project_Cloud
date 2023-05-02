from django.contrib import admin
from .models import Product,SmartPhones,SmartWatches,Televisions

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('Category',)
admin.site.register(Product,ProductAdmin)

class SmartPhone_admin(admin.ModelAdmin):
    list_display = ('ProductName','BrandName','ReleasedDate','AverageCost','Description','Image',)
admin.site.register(SmartPhones,SmartPhone_admin)

class SmartWatch_admin(admin.ModelAdmin):
    list_display = ('ProductName','BrandName','ReleasedDate','AverageCost','Description','Image',)
admin.site.register(SmartWatches,SmartWatch_admin)

class Television_admin(admin.ModelAdmin):
    list_display = ('ProductName','BrandName','ReleasedDate','AverageCost','Description','Image',)
admin.site.register(Televisions,Television_admin)
