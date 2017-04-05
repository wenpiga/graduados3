from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User



class Alumno(models.Model):

	nit= models.CharField(max_length=20)
	nombres= models.CharField(max_length=200)
	programa= models.CharField(max_length=50)
	libro= models.CharField(max_length=10)
	acta= models.CharField(max_length=10)
	folio=models.CharField(max_length=200)
	fecha=models.DateTimeField()
	diploma=models.CharField(max_length=200)
	sede = models.CharField(max_length=200)
	asistencia= models.BooleanField()


	class Meta:
		db_table='alumno'

		

	def __str__(self):
		return '%s "  " %s' % (self.nombres, self.programa)	
		

class Programa(models.Model):
	nombre = models.CharField(max_length=200)

	class Meta:
		db_table= 'programa'

	def __unicode__(self):
		return self.nombre

class userProfile(models.Model):
	def url(self,filename):
		ruta = "MultimediaData/Users/%s/%s"%(self.user.username,filename)
		#ruta = "%s" % (self.user.username, filename)
			
		return	ruta
	user 		=	models.OneToOneField(User)
	foto		=	models.ImageField(upload_to =url)
	telefono	=	models.CharField(max_length=30)
	def __unicode__(self):
		return self.user.username


