from django.contrib import admin
from delivermodels.models import Post, Question, Answer

# Register your models here.

admin.site.register((Post, Question, Answer))