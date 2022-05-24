from distutils.command.upload import upload
from django.db import models

# Create your models here.
class notificacion(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    fecha_publicacion = models.DateField()
    imagen =models.ImageField(upload_to="notificaciones", null=True)
    def __str__(self):
        return self.titulo
    
opciones_consultas=[
    [0,"consulta"],
    [1,"reclamos"],
    [2,"sugerencias" ],
    [3,"felicitaciones" ],
]

class Contacto (models.Model):
    nombre =models.CharField(max_length=30)
    correo = models.EmailField()
    tipo_consulta =models.IntegerField(choices=opciones_consultas)
    mensaje =models.TextField(null=True)
    def __str__(self):
        return self.nombre
    
class estado_cuenta(models.Model):
    mes=models.CharField(max_length=20,null=True)
    montoapagar=models.IntegerField()
    morosidad=models.BooleanField(null=True)
    def __str__(self):
            return self.mes

class area(models.Model):
    nombre=models.CharField(max_length=30)
    imagen=models.ImageField(upload_to="areas",null=True)
    valor=models.IntegerField()
    def __str__(self):
            return self.nombre
        
class residente(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    correo=models.EmailField()
    n_departamento=models.IntegerField()
    estado=models.ForeignKey(estado_cuenta,null=True,on_delete=models.PROTECT)
    def __str__(self):
            return self.nombre

class reserva(models.Model):
    residente=models.ForeignKey(residente,on_delete=models.PROTECT)
    area=models.ForeignKey(area,on_delete=models.PROTECT)
    fecha=models.DateTimeField()
    def __str__(self):
            return self.residente

class pago_reserva(models.Model):
    reserva=models.ForeignKey(reserva,on_delete=models.PROTECT)
    forma_pago=models.CharField(max_length=100000)
    def __str__(self):
            return self.forma_pago

class pago_estado(models.Model):
    estado_cuenta=models.ForeignKey(estado_cuenta,on_delete=models.PROTECT)
    forma_pago=models.CharField(max_length=100000)
    def __str__(self):
            return self.forma_pago

class  horario(models.Model):
    dia=models.CharField(max_length=20)
    hora_inicio=models.CharField(max_length=10)
    hora_termino=models.CharField(max_length=10)
    id_area=models.ForeignKey(area,on_delete=models.PROTECT)
    def __str__(self):
            return self.dia
