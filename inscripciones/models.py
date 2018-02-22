from django.db import models

# Create your models here.

GENEROS=(("M","Masculino"),("F","Femenino"))
SI_NO=(("Si","Si"),("No","No"))
PARENTESCO=(("Esposos","Esposos"),("Novios","Novios"),("Hermanos","Hermanos"),("Primos","Primos"),("Padre/Madre","Padre/Madre"),("Hijo/Hija","Hijo/Hija"),("Otro","Otro"))
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
    id = models.CharField(max_length=6, primary_key=True, default=pkgen)
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
    team = models.CharField(max_length=200, blank='true', null='true')
    observaciones = models.TextField(max_length=500, blank='true', null='true')