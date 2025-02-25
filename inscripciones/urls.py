from django.conf.urls import url
from . import views
from inscripciones.views import PDF
from django.conf.urls import handler404
#from app.views import mi_error_404, ReportePersonasExcel
 
#handler404 = mi_error_404

urlpatterns = [
    url(r'^$',  views.index),
    url(r'^encuesta/$',  views.encuesta),
    url(r'^resultados/$',  views.resultados),
    url(r'^lideres/(?P<cedula>.*)$',  views.lideres_menu),
    url(r'^celula/(?P<cedula>.*)/(?P<id_celula>.*)$',  views.lideres_form),
    url(r'^infocelula/(?P<id_celula>.*)$',  views.lideres_info),
    url(r'^playlist/$',  views.playlist),
    url(r'^success/(?P<id>.*)$', views.success, name='success'),
    url(r'^successlideres/$', views.successlideres, name='successlideres'),
    url(r'^teams/$', views.teams, name='teams'),
    url(r'^pdf/(?P<id>.*)$', PDF.as_view(), name='pdf'),
    url(r'^pagar/(?P<id>.*)$', views.pagar, name='marcar_pagado'),
    #url(r'^2018/', views.inscripciones),
    url(r'^lideres-map/$', views.lideres_map, name='map'),
]