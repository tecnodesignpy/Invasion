from django.contrib import admin
from . import models
#Para el boton de EXPORTAR
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ExportMixin

# Para los boton de ACCIONES
from django.utils.html import format_html
from django.core.urlresolvers import reverse


class FomularioResource(resources.ModelResource):

    class Meta:
        model = models.formulario

class FormularioAdmin(ExportMixin, admin.ModelAdmin):
    list_display = (u'id','nombres','apellidos','team','edad','acompanado','nombre_compania','parentesco','pagado','fecha_pagado','observaciones','usuario_pago','account_actions',)
    list_filter = ('usuario_pago','pagado','capitan','staff','colaborador')
    search_fields = ['id','lider_celula','nombres','cedula','apellidos','telefono','fecha_pagado']
    ordering = ('nombres',)
    save_on_top = True
    readonly_fields = ['fecha_pagado']
    show_full_result_count = True
    resource_class = FomularioResource

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

    def edad(self, obj):
        print(obj.count)
        return obj.count 

class LideresResource(resources.ModelResource):

    class Meta:
        model = models.lideres

class LideresAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (u'id','nombres',)
    ordering = ('nombres',)
    save_on_top = True
    resource_class = LideresResource

class LogradoResource(resources.ModelResource):

    class Meta:
        model = models.logrado

class LogradoAdmin(ExportMixin, admin.ModelAdmin):
    list_display = (u'id','lider',)
    resource_class = LogradoResource

def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.formulario,FormularioAdmin)
_register(models.lideres,LideresAdmin)
_register(models.logrado,LogradoAdmin)
