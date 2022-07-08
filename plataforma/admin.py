from django.contrib import admin
from .models import Pacientes, DadosPaciente, Refeicao, Opcao

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


class RefeicaoAdmin(admin.ModelAdmin):
    list_display = [
        'paciente', 'titulo', 'horario', 'carboidratos', 'proteinas', 'gorduras'
    ]
    
    
class OpcaoAdmin(admin.ModelAdmin):
    list_display = [
        'refeicao', 'descricao'
    ]
    
    
admin.site.register(Opcao, OpcaoAdmin)
admin.site.register(Refeicao, RefeicaoAdmin)
admin.site.register(Pacientes, PacienteAdmin)
admin.site.register(DadosPaciente, DadosPacienteAdmin)