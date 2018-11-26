from django.db import models

# Create your models here.
class Localidad(models.Model):
	id=models.AutoField(unique=True,primary_key=True)
	nombre=models.CharField(max_length=200)

	def __str__(self):
		return self.nombre

class Agente(models.Model):
	id=models.AutoField(unique=True,primary_key=True)
	nombre=models.CharField(max_length=200)
	apellido=models.CharField(max_length=200)
	documento=models.IntegerField(unique=True)
	fecha_nacimiento=models.DateField()
	id_localidad=models.ForeignKey(Localidad, on_delete=models.CASCADE,verbose_name="Localidad")

	def __str__(self):
		return self.apellido+" "+self.nombre

class Familiar(models.Model):
	id=models.AutoField(unique=True,primary_key=True)
	nombre=models.CharField(max_length=200)
	apellido=models.CharField(max_length=200)
	documento=models.IntegerField(unique=True)
	id_agente=models.ForeignKey(Agente, on_delete=models.CASCADE,verbose_name="Agente")
	id_localidad=models.ForeignKey(Localidad, on_delete=models.CASCADE,verbose_name="Localidad")
	fecha_nacimiento=models.DateField()

	def __str__(self):
		return self.apellido+"/"+self.nombre

class Empresa(models.Model):
	id=models.AutoField(unique=True,primary_key=True)
	nombre=models.CharField(max_length=200)
	cuit=models.IntegerField(unique=True)
	id_localidad=models.ForeignKey(Localidad, on_delete=models.CASCADE,verbose_name="Localidad")
	

	def __str__(self):
		return self.nombre+" / Cuit: "+str(self.cuit)

class Pasaje(models.Model):
	id=models.AutoField(unique=True,primary_key=True)
	id_agente=models.ForeignKey(Agente, on_delete=models.CASCADE,verbose_name="Agente")
	id_empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE,verbose_name="Empresa")
	fecha_emision=models.DateField()
	origen=models.CharField(max_length=200)
	destino=models.CharField(max_length=200)

	def __str__(self):
		return str(self.id)+"/"+self.origen+"-"+self.destino+"/"+self.id_empresa.nombre

