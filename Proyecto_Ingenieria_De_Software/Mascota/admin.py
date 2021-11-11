
from django.contrib import admin
from .models import *

class PerritosAdmin(admin.ModelAdmin):
    list_display = ('nombre','raza','edad','color_pelaje','tamaño')
    list_filter = ('color_pelaje' ,'tamaño')
    search_fields = ('nombre', 'raza','tamaño__tamaños','color_pelaje')

class PerritosIMGAdmin(admin.ModelAdmin):
    list_display = ('perrito','imagen')
    list_filter = ('perrito',)
    search_fields = ('perrito__nombre',)

admin.site.register(Perrito, PerritosAdmin)
admin.site.register(Tamaño)
admin.site.register(PerritoImagenes, PerritosIMGAdmin)

