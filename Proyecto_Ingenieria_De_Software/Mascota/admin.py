
from django.contrib import admin
from .models import *

class PerritosAdmin(admin.ModelAdmin):
    list_display = ('nombre','raza','edad','color_pelaje','tamaño','imagenes')
    list_filter = ('color_pelaje' ,'tamaño')
    search_fields = ('nombre', 'raza','tamaño__tamaños','color_pelaje')


admin.site.register(Perrito, PerritosAdmin)
admin.site.register(Tamaño)

