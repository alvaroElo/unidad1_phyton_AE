from django.contrib import admin
from .models import Categoria, Zona, Dispositivo, Medicion

# Registro básico (todas las tablas aparecen en el panel)
admin.site.register([Categoria, Zona, Medicion])

# Registro avanzado para Dispositivo
@admin.register(Dispositivo)
class DispositivoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "consumo_maximo", "estado", "categoria")
    list_filter = ("estado", "categoria")  # Filtros en el lateral
    search_fields = ("nombre",)             # Buscador por nombre
