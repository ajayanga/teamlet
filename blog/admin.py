from django.contrib import admin
from . import models

# Register your models here.
# admin.site.register(models.Blog)
@admin.register(models.Blog)
class Blogs(admin.ModelAdmin):
    list_display = ['title', 'status']

admin.site.register(models.Category)
