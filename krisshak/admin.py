# <!-- Made By - Asmita Kumari -->

from django.contrib import admin

from .models import Krisshak

# Register your models here.

models_list = [Krisshak]
admin.site.register(models_list)
