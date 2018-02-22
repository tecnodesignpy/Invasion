from django.shortcuts import render, redirect
from .models import *
from .forms import *

#PDF

#Importamos settings para poder tener a la mano la ruta de la carpeta media // Para el PDF
from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from django.views.generic import View
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.platypus import Spacer, SimpleDocTemplate, Table, TableStyle
from reportlab.platypus import Paragraph, Image
from reportlab.lib import colors
from django.http import HttpResponse
# la ruta de los staticfiles
from django.conf import settings

# Create your views here.

def inscripciones(request):
    if request.method == "POST":
    	form = InscripcionForm(request.POST)
    	if form.is_valid():
    		dato = form.save()
    		datos = formulario.objects.get(id=dato.pk)
    		return redirect('inscripcion:equipmentoperator',id=datos.id)
    else:
        form = InscripcionForm()
    return render(request, 'formulario.html',{'form':form})


class PDF(View):
    def cabecera(self,pdf,datos):
        print("##############  HOJA 1  ###################")
        archivo_imagen = 'http://invasion.com.py/static/dist/img/logo.png'
        #Definimos el tamanho de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen, 40, 750, 120,preserveAspectRatio=True)      
		#Establecemos el tamanho de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Helvetica", 13)
		#Dibujamos una cadena en la ubicacion X,Y especificada
        pdf.drawString(170, 800, u"Muchas gracias por completar el formulario")
        pdf.drawString(195, 760, u"CAMPAMENTO INVASION 2018")
        pdf.setFont("Helvetica", 20)
        pdf.drawString(160, 720, u"Código de Pre-Inscripción: "+str(datos.id))
        #Definimos el tamanho de la imagen a cargar y las coordenadas correspondientes
        #pdf.drawImage(perfil_foto, 460, 750, 80,80) 



    def get(self, request, id,  *args, **kwargs):
        print(settings.STATIC_URL)
        datos = formulario.objects.get(id=id)
        print(datos.id)
        #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)
        #Llamo al metodo cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf,datos)
        #self.secciones(pdf,datos)
        #Con show page hacemos un corte de página para pasar a la siguiente
        pdf.showPage()
		
		
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response