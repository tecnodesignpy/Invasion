from django.conf.urls import url
from . import views
from inscripciones.views import PDF
from django.conf.urls import handler404
#from app.views import mi_error_404, ReportePersonasExcel
 
#handler404 = mi_error_404

urlpatterns = [
    url(r'^$',  views.inscripciones),
    #url(r'^success/(?P<id>.*)$', views.success, name='success'),
    url(r'^pdf/(?P<id>.*)$', PDF.as_view(), name='equipmentoperator'),
    #url(r'^2018/', views.inscripciones),
]