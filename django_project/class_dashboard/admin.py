from django.contrib import admin
from .models import Logo, Class

# Register your models here.

class LogoAdmin (admin.ModelAdmin): 
    list_display = ['type', 'image', 'color'] 
    ordering = ['type'] 
    list_filter = ['type']

admin.site.register(Logo, LogoAdmin)

class ClassAdmin (admin.ModelAdmin): 
    list_display = ['type', 'name', 'active', 'logo'] 
    ordering = ['type', '-name'] 
    list_filter = ['active', 'type']

admin.site.register(Class, ClassAdmin)