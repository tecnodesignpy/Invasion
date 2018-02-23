from django.contrib import admin
from . import models

# Para los boton de ACCIONES
from django.utils.html import format_html
from django.core.urlresolvers import reverse

	
class FormularioAdmin(admin.ModelAdmin):
    list_display = (u'id','fecha_completado','nombres','apellidos','edad','nacimiento','lider_celula','pagado','fecha_pagado','account_actions',)
    #list_filter = (EdadFilter,NacionalidadFilter,'genero','nivel_ingles','experiencia_years','fumador','licencia_usa','recontratado','trabajo',)
    search_fields = ['id','lider_celula','nombres','cedula','apellidos']
    ordering = ('nombres',)
    save_on_top = True
    readonly_fields = ['fecha_pagado']

    def account_actions(self, obj):
        print(obj.fecha_pagado)
        if(obj.fecha_pagado == None or obj.pagado == False):
            return format_html(
                '<a class="button" style="background-color:green" href="{}">Pagar</a>&nbsp;'
                '<a class="button" href="{}">PDF</a>&nbsp;',
                reverse('inscripcion:marcar_pagado', args=[obj.pk]),
                reverse('inscripcion:pdf', args=[obj.pk]),
            )
        else:
            return format_html(
                '<a class="button" href="{}">PDF</a>&nbsp;',
                reverse('inscripcion:pdf', args=[obj.pk]),
            )
    account_actions.short_description = 'Botones'
    account_actions.allow_tags = True

def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.formulario,FormularioAdmin)
