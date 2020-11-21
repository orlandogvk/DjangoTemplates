from django.contrib import admin
from clases.models import Clase

# Register your models here.


class ClasesAdmin(admin.ModelAdmin):
    list_display =("nombre","salon")
    search_fields =("nombre",)

admin.site.register(Clase,ClasesAdmin)

