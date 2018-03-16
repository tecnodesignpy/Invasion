from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.contrib.auth.decorators import login_required

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
import random
from random import shuffle

#import locale 
# Definimos el formato que deseamos
#locale.setlocale(locale.LC_ALL, 'es_ES')
#locale.setlocale(locale.LC_ALL, 'en_US')
#locale.setlocale(locale.LC_ALL, '')


# la ruta de los staticfiles
from django.conf import settings

# Create your views here.

@csrf_exempt
def inscripciones(request):
    if request.method == "POST":
    	form = InscripcionForm(request.POST)
    	if form.is_valid():
    		dato = form.save()
    		datos = formulario.objects.get(id=dato.pk)
    		return redirect('inscripcion:success',id=datos.id)
    else:
        form = InscripcionForm()
    return render(request, 'formulario.html',{'form':form})

def success(request,id):
    codigo=id
    return render(request, 'success.html',{'codigo':codigo})

@login_required(login_url='/admin')
def pagar(request,id):
    codigo=id
    current_user = request.user
    print(current_user.first_name)
    datos = formulario.objects.get(id=codigo)
    datos.fecha_pagado = datetime.now()
    datos.pagado = True
    datos.usuario_pago = current_user.first_name
    datos.save()
    return redirect('/admin/inscripciones/formulario/')

@login_required(login_url='/admin')
def teams(request):
    persona = formulario.objects.filter(pagado=True, capitan=False, colaborador=False, staff=False)
    #persona = formulario.objects.filter()
    # Declaramos los arrays para cada team
    ovejas = []
    leones = []
    bufalos = []
    aguilas = []
    iterable = []
    edad1 = 0
    edad2 = 0
    edad3 = 0
    edad4 = 0
    edad_oveja1 = 0
    edad_oveja2 = 0
    edad_oveja3 = 0
    edad_oveja4 = 0
    edad_leones1 = 0
    edad_leones2 = 0
    edad_leones3 = 0
    edad_leones4 = 0
    edad_bufalos1 = 0
    edad_bufalos2 = 0
    edad_bufalos3 = 0
    edad_bufalos4 = 0
    edad_aguilas1 = 0
    edad_aguilas2 = 0
    edad_aguilas3 = 0
    edad_aguilas4 = 0
    masculino1 = 0
    femenino1 = 0
    masculino2 = 0
    femenino2 = 0
    masculino3 = 0
    femenino3 = 0
    masculino4 = 0
    femenino4 = 0
    masculino_ovejas1 = 0
    masculino_ovejas2 = 0
    masculino_ovejas3 = 0
    masculino_ovejas4 = 0
    masculino_leones1 = 0
    masculino_leones2 = 0
    masculino_leones3 = 0
    masculino_leones4 = 0
    masculino_bufalos1 = 0
    masculino_bufalos2 = 0
    masculino_bufalos3 = 0
    masculino_bufalos4 = 0
    masculino_aguilas1 = 0
    masculino_aguilas2 = 0
    masculino_aguilas3 = 0
    masculino_aguilas4 = 0
    femenino_ovejas1 = 0
    femenino_ovejas2 = 0
    femenino_ovejas3 = 0
    femenino_ovejas4 = 0
    femenino_leones1 = 0
    femenino_leones2 = 0
    femenino_leones3 = 0
    femenino_leones4 = 0
    femenino_bufalos1 = 0
    femenino_bufalos2 = 0
    femenino_bufalos3 = 0
    femenino_bufalos4 = 0
    femenino_aguilas1 = 0
    femenino_aguilas2 = 0
    femenino_aguilas3 = 0
    femenino_aguilas4 = 0
    # Hacemos la division por equipos
    division = int(round(len(persona)/4))
    # Creamos una variable nueva donde luego le aplicamos suffle() para cambiar el orden de la lista
    for p in persona:
        iterable.append(p)
        if(int(p.edad) >= 12 and int(p.edad) <= 17):
            edad1= edad1 +1
            if(p.sexo == "M"):
                masculino1 = masculino1 + 1
            else:
                femenino1 = femenino1 + 1
        if(int(p.edad) >= 18 and int(p.edad) <= 24):
            edad2= edad2 +1
            if(p.sexo == "M"):
                masculino2 = masculino2 + 1
            else:
                femenino2 = femenino2 + 1
        if(int(p.edad) >= 25 and int(p.edad) <= 32):
            edad3= edad3 +1
            if(p.sexo == "M"):
                masculino3 = masculino3 + 1
            else:
                femenino3 = femenino3 + 1
        if(int(p.edad) >= 33 and int(p.edad) <= 40):
            edad4= edad4 +1
            if(p.sexo == "M"):
                masculino4 = masculino4 + 1
            else:
                femenino4 = femenino4 + 1
    # Cambiamos el orden de la lista recien creada, de manera random
    shuffle(iterable)
    # Recorremos el array "iterable" que tiene una lista ordenada de manera random
    suma = 0
    for p in iterable:
        if((len(ovejas) <= division) and (len(ovejas) <= len(leones) and len(ovejas) <= len(bufalos) and len(ovejas) <= len(aguilas)) ):
            if((int(p.edad) >= 12 and int(p.edad) <= 17) and (int(edad_oveja1) <= round((edad1/4)))):
                if(p.sexo == "M" and masculino_ovejas1 < round(masculino1/4)):
                    ovejas.append(p.id)
                    datos = formulario.objects.get(id=p.id)
                    datos.team = "Ovejas"
                    datos.save()
                    masculino_ovejas1 = masculino_ovejas1 +1
                    edad_oveja1 = edad_oveja1 +1
                elif(p.sexo == "F" and femenino_ovejas1 < round(femenino1/4)):
                    ovejas.append(p.id)
                    datos = formulario.objects.get(id=p.id)
                    datos.team = "Ovejas"
                    datos.save()
                    femenino_ovejas1 = femenino_ovejas1 +1
                    edad_oveja1 = edad_oveja1 +1
            elif((int(p.edad) >= 18 and int(p.edad) <= 24) and (int(edad_oveja2) <= round((edad2/4)))):
                if(p.sexo == "M" and masculino_ovejas2 < round(masculino2/4)):
                    ovejas.append(p.id)
                    datos = formulario.objects.get(id=p.id)
                    datos.team = "Ovejas"
                    datos.save()
                    masculino_ovejas2 = masculino_ovejas2 +1
                    edad_oveja2 = edad_oveja2 +1
                elif(p.sexo == "F" and femenino_ovejas2 < round(femenino2/4)):
                    ovejas.append(p.id)
                    datos = formulario.objects.get(id=p.id)
                    datos.team = "Ovejas"
                    datos.save()
                    femenino_ovejas2 = femenino_ovejas2 +1
                    edad_oveja2 = edad_oveja2 +1
            elif((int(p.edad) >= 25 and int(p.edad) <= 32) and (int(edad_oveja3) <= round((edad3/4)))):
                if(p.sexo == "M" and masculino_ovejas3 < round(masculino3/4)):
                    ovejas.append(p.id)
                    datos = formulario.objects.get(id=p.id)
                    datos.team = "Ovejas"
                    datos.save()
                    masculino_ovejas3 = masculino_ovejas3 +1
                    edad_oveja3 = edad_oveja3 +1
                elif(p.sexo == "F" and femenino_ovejas3 < round(femenino3/4)):
                    ovejas.append(p.id)
                    datos = formulario.objects.get(id=p.id)
                    datos.team = "Ovejas"
                    datos.save()
                    femenino_ovejas3 = femenino_ovejas3 +1
                    edad_oveja3 = edad_oveja3 +1
            elif((int(p.edad) >= 33 and int(p.edad) <= 40) and (int(edad_oveja4) <= round((edad4/4)))):
                if(p.sexo == "M" and masculino_ovejas4 < round(masculino4/4)):
                    ovejas.append(p.id)
                    datos = formulario.objects.get(id=p.id)
                    datos.team = "Ovejas"
                    datos.save()
                    masculino_ovejas4 = masculino_ovejas4 +1
                    edad_oveja4 = edad_oveja4 +1
                elif(p.sexo == "F" and femenino_ovejas4 < round(femenino4/4)):
                    ovejas.append(p.id)
                    datos = formulario.objects.get(id=p.id)
                    datos.team = "Ovejas"
                    datos.save()
                    femenino_ovejas4 = femenino_ovejas4 +1
                    edad_oveja4 = edad_oveja4 +1
            else:
                datos = formulario.objects.get(id=p.id)
                datos.team = "Leones"
                datos.save()
        elif((len(leones) <= division) and (len(leones) <= len(ovejas) and len(leones) <= len(bufalos) and len(leones) <= len(aguilas)) ):
            if((int(p.edad) >= 12 and int(p.edad) <= 17) and (int(edad_leones1) <= round((edad1/4)))):
                if(p.sexo == "M" and masculino_leones1 < round(masculino1/4)):
                    leones.append(p.id)
                    datos = formulario.objects.get(id=p.id)
                    datos.team = "Leones"
                    datos.save()
                    masculino_leones1 = masculino_leones1 +1
                    edad_leones1 = edad_leones1 +1
                elif(p.sexo == "F" and femenino_leones1 < round(femenino1/4)):
                    leones.append(p.id)
                    datos = formulario.objects.get(id=p.id)
                    datos.team = "Leones"
                    datos.save()
                    femenino_leones1 = femenino_leones1 +1
                    edad_leones1 = edad_leones1 +1
            elif((int(p.edad) >= 18 and int(p.edad) <= 24) and (int(edad_leones2) <= round((edad2/4)))):
                if(p.sexo == "M" and masculino_leones2 < round(masculino2/4)):
                    leones.append(p.id)
                    datos = formulario.objects.get(id=p.id)
                    datos.team = "Leones"
                    datos.save()
                    masculino_leones2 = masculino_leones2 +1
                    edad_leones2 = edad_leones2 +1
                elif(p.sexo == "F" and femenino_leones2 < round(femenino2/4)):
                    leones.append(p.id)
                    datos = formulario.objects.get(id=p.id)
                    datos.team = "Leones"
                    datos.save()
                    femenino_leones2 = femenino_leones2 +1
                    edad_leones2 = edad_leones2 +1
            elif((int(p.edad) >= 25 and int(p.edad) <= 32) and (int(edad_leones3) <= round((edad3/4)))):
                if(p.sexo == "M" and masculino_leones3 < round(masculino3/4)):
                    leones.append(p.id)
                    datos = formulario.objects.get(id=p.id)
                    datos.team = "Leones"
                    datos.save()
                    masculino_leones3 = masculino_leones3 +1
                    edad_leones3 = edad_leones3 +1
                elif(p.sexo == "F" and femenino_leones3 < round(femenino3/4)):
                    leones.append(p.id)
                    datos = formulario.objects.get(id=p.id)
                    datos.team = "Leones"
                    datos.save()
                    femenino_leones3 = femenino_leones3 +1
                    edad_leones3 = edad_leones3 +1
            elif((int(p.edad) >= 33 and int(p.edad) <= 40) and (int(edad_leones4) <= round((edad4/4)))):
                if(p.sexo == "M" and masculino_leones4 < round(masculino4/4)):
                    leones.append(p.id)
                    datos = formulario.objects.get(id=p.id)
                    datos.team = "Leones"
                    datos.save()
                    masculino_leones4 = masculino_leones4 +1
                    edad_leones4 = edad_leones4 +1
                elif(p.sexo == "F" and femenino_leones4 < round(femenino4/4)):
                    leones.append(p.id)
                    datos = formulario.objects.get(id=p.id)
                    datos.team = "Leones"
                    datos.save()
                    femenino_leones4 = femenino_leones4 +1
                    edad_leones4 = edad_leones4 +1
            else:
                datos = formulario.objects.get(id=p.id)
                datos.team = "Bufalos"
                datos.save()
        elif((len(bufalos) <= division) and (len(bufalos) <= len(ovejas) and len(bufalos) <= len(leones) and len(bufalos) <= len(aguilas)) ):            
            if((int(p.edad) >= 12 and int(p.edad) <= 17) and (int(edad_bufalos1) <= round((edad1/4)))):
                if(p.sexo == "M" and masculino_bufalos1 < round(masculino1/4)):
                    bufalos.append(p.id)
                    datos = formulario.objects.get(id=p.id)
                    datos.team = "Bufalos"
                    datos.save()
                    masculino_bufalos1 = masculino_bufalos1 +1
                    edad_bufalos1 = edad_bufalos1 +1
                elif(p.sexo == "F" and femenino_bufalos1 < round(femenino1/4)):
                    bufalos.append(p.id)
                    datos = formulario.objects.get(id=p.id)
                    datos.team = "Bufalos"
                    datos.save()
                    femenino_bufalos1 = femenino_bufalos1 +1
                    edad_bufalos1 = edad_bufalos1 +1
            elif((int(p.edad) >= 18 and int(p.edad) <= 24) and (int(edad_bufalos2) <= round((edad2/4)))):
                if(p.sexo == "M" and masculino_bufalos2 < round(masculino2/4)):
                    bufalos.append(p.id)
                    datos = formulario.objects.get(id=p.id)
                    datos.team = "Bufalos"
                    datos.save()
                    masculino_bufalos2 = masculino_bufalos2 +1
                    edad_bufalos2 = edad_bufalos2 +1
                elif(p.sexo == "F" and femenino_bufalos2 < round(femenino2/4)):
                    bufalos.append(p.id)
                    datos = formulario.objects.get(id=p.id)
                    datos.team = "Bufalos"
                    datos.save()
                    femenino_bufalos2 = femenino_bufalos2 +1
                    edad_bufalos2 = edad_bufalos2 +1
            elif((int(p.edad) >= 25 and int(p.edad) <= 32) and (int(edad_bufalos3) <= round((edad3/4)))):
                if(p.sexo == "M" and masculino_bufalos3 < round(masculino3/4)):
                    bufalos.append(p.id)
                    datos = formulario.objects.get(id=p.id)
                    datos.team = "Bufalos"
                    datos.save()
                    masculino_bufalos3 = masculino_bufalos3 +1
                    edad_bufalos3 = edad_bufalos3 +1
                elif(p.sexo == "F" and femenino_bufalos3 < round(femenino3/4)):
                    bufalos.append(p.id)
                    datos = formulario.objects.get(id=p.id)
                    datos.team = "Bufalos"
                    datos.save()
                    femenino_bufalos3 = femenino_bufalos3 +1
                    edad_bufalos3 = edad_bufalos3 +1
            elif((int(p.edad) >= 33 and int(p.edad) <= 40) and (int(edad_bufalos4) <= round((edad4/4)))):
                if(p.sexo == "M" and masculino_bufalos4 < round(masculino4/4)):
                    bufalos.append(p.id)
                    datos = formulario.objects.get(id=p.id)
                    datos.team = "Bufalos"
                    datos.save()
                    masculino_bufalos4 = masculino_bufalos4 +1
                    edad_bufalos4 = edad_bufalos4 +1
                elif(p.sexo == "F" and femenino_bufalos4 < round(femenino4/4)):
                    bufalos.append(p.id)
                    datos = formulario.objects.get(id=p.id)
                    datos.team = "Bufalos"
                    datos.save()
                    femenino_bufalos4 = femenino_bufalos4 +1
                    edad_bufalos4 = edad_bufalos4 +1
            else:
                datos = formulario.objects.get(id=p.id)
                datos.team = "Aguilas"
                datos.save()
        elif((len(aguilas) <= division) and (len(aguilas) <= len(ovejas) and len(aguilas) <= len(bufalos) and len(aguilas) <= len(leones)) ):
            if((int(p.edad) >= 12 and int(p.edad) <= 17) and (int(edad_aguilas1) <= round((edad1/4)))):
                if(p.sexo == "M" and masculino_aguilas1 < round(masculino1/4)):
                    aguilas.append(p.id)
                    datos = formulario.objects.get(id=p.id)
                    datos.team = "Aguilas"
                    datos.save()
                    masculino_aguilas1 = masculino_aguilas1 +1
                    edad_aguilas1 = edad_aguilas1 +1
                elif(p.sexo == "F" and femenino_aguilas1 < round(femenino1/4)):
                    aguilas.append(p.id)
                    datos = formulario.objects.get(id=p.id)
                    datos.team = "Aguilas"
                    datos.save()
                    femenino_aguilas1 = femenino_aguilas1 +1
                    edad_aguilas1 = edad_aguilas1 +1
            elif((int(p.edad) >= 18 and int(p.edad) <= 24) and (int(edad_aguilas2) <= round((edad2/4)))):
                if(p.sexo == "M" and masculino_aguilas2 < round(masculino2/4)):
                    aguilas.append(p.id)
                    datos = formulario.objects.get(id=p.id)
                    datos.team = "Aguilas"
                    datos.save()
                    masculino_aguilas2 = masculino_aguilas2 +1
                    edad_aguilas2 = edad_aguilas2 +1
                elif(p.sexo == "F" and femenino_aguilas2 < round(femenino2/4)):
                    aguilas.append(p.id)
                    datos = formulario.objects.get(id=p.id)
                    datos.team = "Aguilas"
                    datos.save()
                    femenino_aguilas2 = femenino_aguilas2 +1
                    edad_aguilas2 = edad_aguilas2 +1
            elif((int(p.edad) >= 25 and int(p.edad) <= 32) and (int(edad_aguilas3) <= round((edad3/4)))):
                if(p.sexo == "M" and masculino_aguilas3 < round(masculino3/4)):
                    aguilas.append(p.id)
                    datos = formulario.objects.get(id=p.id)
                    datos.team = "Aguilas"
                    datos.save()
                    masculino_aguilas3 = masculino_aguilas3 +1
                    edad_aguilas3 = edad_aguilas3 +1
                elif(p.sexo == "F" and femenino_aguilas3 < round(femenino3/4)):
                    aguilas.append(p.id)
                    datos = formulario.objects.get(id=p.id)
                    datos.team = "Aguilas"
                    datos.save()
                    femenino_aguilas3 = femenino_aguilas3 +1
                    edad_aguilas3 = edad_aguilas3 +1
            elif((int(p.edad) >= 33 and int(p.edad) <= 40) and (int(edad_aguilas4) <= round((edad4/4)))):
                if(p.sexo == "M" and masculino_aguilas4 < round(masculino4/4)):
                    aguilas.append(p.id)
                    datos = formulario.objects.get(id=p.id)
                    datos.team = "Aguilas"
                    datos.save()
                    masculino_aguilas4 = masculino_aguilas4 +1
                    edad_aguilas4 = edad_aguilas4 +1
                elif(p.sexo == "F" and femenino_aguilas4 < round(femenino4/4)):
                    aguilas.append(p.id)
                    datos = formulario.objects.get(id=p.id)
                    datos.team = "Aguilas"
                    datos.save()
                    femenino_aguilas4 = femenino_aguilas4 +1
                    edad_aguilas4 = edad_aguilas4 +1
            else:
                datos = formulario.objects.get(id=p.id)
                datos.team = "Ovejas"
                datos.save()
    # Redireccionamos solo el listado de acampantes pagados, que no son capitanes, ni staff, ni colaboradores
    return redirect('/admin/inscripciones/formulario/?all=&capitan__exact=0&colaborador__exact=0&o=4.5&pagado__exact=1&staff__exact=0')

class PDF(View):
    def cabecera(self,pdf,datos):
        print("##############  HOJA 1  ###################")
        archivo_imagen = 'http://invasion.com.py/static/dist/img/logo.png'
        print(archivo_imagen)
        #Definimos el tamanho de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen, 160, -400, 80,preserveAspectRatio=True)      
		#Establecemos el tamanho de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Helvetica", 13)
		#Dibujamos una cadena en la ubicacion X,Y especificada
        pdf.drawString(110, 170, u"CAMPAMENTO INVASION 2018")
        pdf.setFont("Helvetica-Bold", 20)
        pdf.drawString(55, 80, u"Código de Pre-Inscripción: "+str(datos.id))
        pdf.setFont("Helvetica", 13)
        pdf.drawString(40, 60, u"Nombre y Apellido: "+ str(datos.nombres) +" "+ str(datos.apellidos))
        pdf.drawString(40, 40, u"CI: "+ format(int(datos.cedula),','))
        pdf.setFillColorRGB(255,0,0) #choose your font colour
        pdf.drawString(40, 20, u"No olvides abonar el monto para validar tu inscripción!")
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
        pdf.setPageSize((400, 200))
        self.cabecera(pdf,datos)
        #self.secciones(pdf,datos)
        #Con show page hacemos un corte de página para pasar a la siguiente
        pdf.showPage()
		
		
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response


