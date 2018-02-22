from django.contrib import admin
from . import models

# Para los boton de ACCIONES
from django.utils.html import format_html
from django.core.urlresolvers import reverse

class EdadFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = ('Age')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'edad'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('1', '18-25'),
            ('2', '26-35'),
            ('3', '36-40'),
            ('4', '41+'),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == '1':
            return queryset.filter(edad__gte=18,
                                    edad__lte=25)
        if self.value() == '2':
            return queryset.filter(edad__gte=26,
                                    edad__lte=35)
        if self.value() == '3':
            return queryset.filter(edad__gte=36,
                                    edad__lte=40)
        if self.value() == '4':
            return queryset.filter(edad__gte=41,
                                    edad__lte=99)

	
class FormularioAdmin(admin.ModelAdmin):
    list_display = (u'id','fecha_completado','nombres','apellidos','edad','nacimiento','pagado','fecha_pagado','account_actions',)
    #list_filter = (EdadFilter,NacionalidadFilter,'genero','nivel_ingles','experiencia_years','fumador','licencia_usa','recontratado','trabajo',)
    #search_fields = ['pais','nombres','edad','id','apellidos','experiencia','company_name','Experiencia_Laboral','comment','hear_about','recrutier','conocimiento_mecanica','consulado_cercano','ciudad','calle_nombre','email','status','genero','facebook_name','skype_name',]
    ordering = ('-fecha_completado',)
    save_on_top = True

    def account_actions(self, obj):
        print(obj.fecha_pagado)
        if(obj.fecha_pagado == None):
            return format_html(
                '<a class="button" style="background-color:green" onclick="marcar_pagado()">Pagar</a>&nbsp;'
                '<a class="button" href="{}">PDF</a>&nbsp;',
                reverse('inscripcion:pdf', args=[obj.pk]),
                reverse('inscripcion:pdf', args=[obj.pk]),
            )
        else:
            return format_html(
                '<a class="button" href="{}">PDF</a>&nbsp;',
                reverse('inscripcion:pdf', args=[obj.pk]),
            )
    account_actions.short_description = 'Botones'
    account_actions.allow_tags = True

    def marcar_pagado(self, request, queryset):
        rows_updated = queryset.update(status='p')
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)


def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.formulario,FormularioAdmin)
