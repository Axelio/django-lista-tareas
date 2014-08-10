from django.contrib import admin

from models import Tarea, TareaDetalle, Categoria

admin.site.register(Tarea)
class TareaDetalleAdmin(admin.ModelAdmin):
    list_filter = ('tarea__categoria', 'cumplida')
    list_display = ('usuario', 'tarea', 'cumplida')
admin.site.register(TareaDetalle, TareaDetalleAdmin)
admin.site.register(Categoria)
