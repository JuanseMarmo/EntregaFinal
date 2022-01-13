from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Auto)

admin.site.register(Moto)

admin.site.register(Camion)

admin.site.register(Vender)

