from atexit import register
from django.contrib import admin

from general.models import CustomUser

# Register your models here.
admin.site.register(CustomUser)