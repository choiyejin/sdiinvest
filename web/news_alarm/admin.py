from django.contrib import admin
from .models import News
from .models import Stock

# Register your models here.
admin.site.register(News)
admin.site.register(Stock)