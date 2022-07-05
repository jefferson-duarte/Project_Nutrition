from django.contrib import admin
from .models import Ativacao


class AtivacaoAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'token',
        'ativo',
    ]
    
    list_editable = [
        'ativo',
    ]
    

admin.site.register(Ativacao, AtivacaoAdmin)