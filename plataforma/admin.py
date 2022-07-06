from django.contrib import admin
from .models import Pacientes

class PacienteAdmin(admin.ModelAdmin):
    list_display = [
        'nome', 'idade', 'sexo', 'telefone', 'email', 'nutri',    
    ]
    
    list_editable = [
        'telefone', 'email', 'nutri',
    ]
    
admin.site.register(Pacientes, PacienteAdmin)
