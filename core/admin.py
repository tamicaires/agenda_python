from django.contrib import admin
from core.models import Evento

class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_evento', 'data_criacao', 'usuario')
    #list_filter = ('usuario', 'data_evento')


admin.site.register(Evento, EventoAdmin)