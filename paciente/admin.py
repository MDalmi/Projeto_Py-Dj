from django.contrib import admin

from medico.models import Documento
from .models import Consulta
# Register your models here.

admin.site.register(Consulta)
admin.site.register(Documento)