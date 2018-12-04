from django.contrib import admin
from delivermodels.models import Product, Batch, Post, Comment

# Register your models here.

admin.site.register((Product, Batch, Post, Comment))