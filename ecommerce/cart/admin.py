from django.contrib import admin

# Register your models here.
from cart.models import Cart,Order,Account
admin.site.register(Cart)
admin.site.register(Account)
admin.site.register(Order)