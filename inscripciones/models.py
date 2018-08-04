from django.db import models
from randomslugfield import RandomSlugField

# Create your models here.

GENEROS=(("M","Masculino"),("F","Femenino"))
SI_NO=(("Si","Si"),("No","No"))
PARENTESCO=(("Esposos","Esposos"),("Novios","Novios"),("Hermanos","Hermanos"),("Primos","Primos"),("Papa/Mama","Papá/Mamá"),("Hijo/Hija","Hijo/Hija"),("Otro","Otro"))
REMERAS=(("P","P"),("M","M"),("G","G"),("XG","XG"))

def pkgen():
    from base64 import b32encode
    from hashlib import sha1
    import string, random
    import hashlib
    rude = ('lol',)
    bad_pk = True
    while bad_pk:
        pk = hashlib.sha256(str(random.random()).encode('utf-8')).hexdigest().lower()[:3]
        bad_pk = False
        for rw in rude:
            if pk.find(rw) >= 0: bad_pk = True
    return pk

class formulario(models.Model):
	#Seccion 1
    id = RandomSlugField(length=3, exclude_upper=True, exclude_vowels=True, primary_key=True)
    nombres = models.CharField(max_length=200, blank='true', null='true',)
    apellidos = models.CharField(max_length=200, blank='true', null='true')
    edad = models.CharField(max_length=10, blank='true', null='true')
    sexo = models.CharField(max_length=20, choices=GENEROS, blank='true', null='true')
    cedula = models.CharField(max_length=200, blank='true', null='true',verbose_name='Cedula')
    nacimiento = models.CharField(max_length=200, blank='true', null='true')
    celula = models.CharField(max_length=200, choices=SI_NO, blank='true', null='true')
    lider_celula = models.CharField(max_length=200, blank='true', null='true')
    domicilio = models.CharField(max_length=200, blank='true', null='true')
    telefono = models.CharField(max_length=200, blank='true', null='true')
    bus_si_no = models.CharField(max_length=200, choices=SI_NO, blank='true', null='true')
    talle_remera = models.CharField(max_length=100, choices=REMERAS, blank='true', null='true')
    primera_vez = models.CharField(max_length=200, choices=SI_NO, blank='true', null='true')
    acompanado = models.CharField(max_length=200, choices=SI_NO, blank='true', null='true')
    parentesco = models.CharField(max_length=200, choices=PARENTESCO, blank='true', null='true')
    nombre_compania = models.CharField(max_length=200, blank='true', null='true')
    fecha_completado = models.DateField(auto_now_add=True)
    pagado = models.BooleanField(default=False)
    capitan = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    colaborador = models.BooleanField(default=False)
    usuario_pago = models.CharField(max_length=200, blank='true', null='true')
    fecha_pagado = models.CharField(max_length=200, blank='true', null='true')
    team = models.CharField(max_length=200, blank='true', null='true')
    observaciones = models.TextField(max_length=500, blank='true', null='true')


    
    def update(self, *args, **kwargs):
        pagado_var = str(self.pagado)
        print(pagado_var)
        if pagado_var == False:
            self.fecha_pagado = ''
        super(formulario, self).save(*args, **kwargs)
    
    def __str__(self):
        return str(self.id) 


class lideres(models.Model):
    nombres = models.CharField(max_length=200, blank='true', null='true',)
    ci = models.CharField(max_length=200, blank='true', null='true',)
    lider = models.CharField(max_length=200, blank='true', null='true',)
    discipulos = models.CharField(max_length=200, blank='true', null='true',)
    ganar = models.CharField(max_length=200, blank='true', null='true',)
    consolidar_agua = models.CharField(max_length=200, blank='true', null='true',)
    consolidar_espiritu = models.CharField(max_length=200, blank='true', null='true',)
    consolidar_seminario = models.CharField(max_length=200, blank='true', null='true',)
    discipular_caminando = models.CharField(max_length=200, blank='true', null='true',)
    discipular_escuela = models.CharField(max_length=200, blank='true', null='true',)
    discipular_imparticion = models.CharField(max_length=200, blank='true', null='true',)
    discipular_vocacional = models.CharField(max_length=200, blank='true', null='true',)
    multiplicar = models.CharField(max_length=200, blank='true', null='true',)
    linea = models.CharField(max_length=200, blank='true', null='true',)
    
    def __str__(self):
        return str(self.nombres) 


class logrado(models.Model):
    lider = models.ForeignKey(lideres, on_delete=models.CASCADE)
    mes = models.CharField(max_length=100, blank='true', null='true',)
    discipulos = models.CharField(max_length=200, blank='true', null='true',)
    ganar = models.CharField(max_length=200, blank='true', null='true',)
    consolidar_agua = models.CharField(max_length=200, blank='true', null='true',)
    consolidar_espiritu = models.CharField(max_length=200, blank='true', null='true',)
    consolidar_seminario = models.CharField(max_length=200, blank='true', null='true',)
    discipular_caminando = models.CharField(max_length=200, blank='true', null='true',)
    discipular_escuela = models.CharField(max_length=200, blank='true', null='true',)
    discipular_imparticion = models.CharField(max_length=200, blank='true', null='true',)
    discipular_vocacional = models.CharField(max_length=200, blank='true', null='true',)
    multiplicar = models.CharField(max_length=200, blank='true', null='true',)
    linea = models.CharField(max_length=200, blank='true', null='true',)
    
    def __str__(self):
        return str(self.lider) 

    def save(self, *args, **kwargs):
            similars = logrado.objects.filter(mes=self.mes, lider=self.lider)
            created = logrado.objects.filter(mes=self.mes, lider=self.lider).count()
            if created != 0:
                print ('exist')
                similars.delete()
                super(logrado, self).save(*args, **kwargs)
            else:
                super(logrado, self).save(*args, **kwargs)





