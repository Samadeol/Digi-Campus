from django.contrib import admin

# Register your models here.
from .models import messMain,messExtras
from .models import messOrder
admin.site.register(messMain)
admin.site.register(messOrder)
admin.site.register(messExtras)