from django.contrib import admin

# Register your models here.
from .models import Categoria, Zona, Dispositivo

admin.site.register([Categoria, Zona])

@admin.register(Dispositivo)
class DispositivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'zona', 'consumo_maximo')
    list_filter = ("estado", "categoria")  # Filtros en el lateral
    search_fields = ("nombre",)             # Buscador por NOMBRE
