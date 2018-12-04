from django.contrib import admin
from .models import DeliverUser, Mayorista
# Register your models here.

admin.site.register((DeliverUser, Mayorista))