from django.contrib import admin
from .models import Pacientes, DadosPaciente

class PacienteAdmin(admin.ModelAdmin):
    list_display = [
        'nome', 'idade', 'sexo', 'telefone', 'email', 'nutri',    
    ]
    
    list_editable = [
        'telefone', 'email', 'nutri',
    ]
    

class DadosPacienteAdmin(admin.ModelAdmin):
    list_display = [
        'paciente', 'data', 'peso', 'altura'
    ]
    
admin.site.register(Pacientes, PacienteAdmin)
admin.site.register(DadosPaciente, DadosPacienteAdmin)