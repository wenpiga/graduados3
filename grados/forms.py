from django import forms
from models import Alumno
from django.contrib.admin import widgets
from models import Programa
from django.forms import ModelForm
from django.contrib.auth.models import User



#from django.forms import modelForm


class ContactForm(forms.Form):
	Email	=	forms.EmailField(widget=forms.TextInput())
	Titulo	=	forms.CharField(widget=forms.TextInput())
	Mensaje	=	forms.CharField(widget=forms.Textarea())



class AddAlumnoForm(forms.Form):
		nit			= forms.CharField(widget=forms.TextInput())
		nombres		= forms.CharField(widget=forms.TextInput())
		programa	= forms.ModelChoiceField(queryset=Programa.objects.all())
		libro		= forms.CharField(widget=forms.TextInput())
		acta		= forms.CharField(widget=forms.TextInput())
		folio		= forms.CharField(widget=forms.TextInput())
		'''fecha		=forms.DateField()'''
		fecha		= forms.DateField(widget=widgets.AdminDateWidget()) 
		diploma		= forms.CharField(widget=forms.TextInput())
		sede		= forms.CharField(widget=forms.TextInput())
		asistencia	= forms.BooleanField(required=False)


		'''class Meta:
			db_table='alumno' '''

		def clean(self):
			return self.cleaned_data


class LoginForm(forms.Form):
	username	=	forms.CharField(widget=forms.TextInput())
	password	=	forms.CharField(widget=forms.PasswordInput(render_value=False))
		


class AlumnoForm(forms.Form):
	
	class Meta:
		model =	Alumno



class ProgramaForm(ModelForm):
	class Meta:
		model = Programa 
		fields = '__all__'

class Miformulario(forms.Form):
	usuario = forms.ModelChoiceField(queryset=User.objects.none())

	def __init__(self,user,*args, ** kwargs):
		super(Miformulario,self).__init__(*args, **kwargs)

		if user.is_superuser:
			self.fields['usuario'].queryset=User.objects.all()
		else:
			self.fields['usuario'].queryset = User.objects.filter(is_staff = True)
			

class ConsultaForm(forms.Form):

	Fecha_Inicial =	forms.DateField(widget=widgets.AdminDateWidget()) 
	Fecha_Final = 	forms.DateField(widget=widgets.AdminDateWidget()) 


	'''def __init__(self, *args, **kwargs):
		super(ConsultaForm,self).__init__(*args, **kwargs)
		self.fields['Fecha_Inicial'].widget = widgets.AdminDateWidget()
		self.fields['Fecha_Final'].widget = widgets.AdminDateWidget()'''




	

from .models import Programa
prog = Programa.objects.all().values_list('nombre', 'nombre')
class Programas(forms.Form):
	programa	= forms.ChoiceField(choices=prog)




	




