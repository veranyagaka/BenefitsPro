from django.contrib import admin

# Register your models here.
from .models import Benefits

admin.site.register(Benefits)

from .models import Application

admin.site.register(Application)