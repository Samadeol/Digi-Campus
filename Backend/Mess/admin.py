from django.contrib import admin

# Register your models here.
from .models import messMenu
from .models import OrderHistory
admin.site.register(messMenu)
admin.site.register(OrderHistory)