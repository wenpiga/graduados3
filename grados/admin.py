from django.contrib import admin
from datetime import datetime, date, time, timedelta
import calendar
from  models import Alumno, Programa,userProfile
from django.contrib.admin.views.decorators import staff_member_required
#from import_export import resources

from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin

from import_export import resources
from import_export import fields
#from django.core.models import Alumno

#from core.models import Alumno



class AlumnoResource(resources.ModelResource):

    class Meta:
        model = Alumno
      
        fields =('nit','nombres','programa','libro','acta','folio','fecha','diploma','sede','asistencia')    	     
        #fields =('get_full_name','id','nit','nombres','programa','libro','acta','folio','fecha.datetime.strptime(date_string, format)','diploma')


class alumnoAdmin(ImportExportActionModelAdmin):

	list_display=('nit','nombres','programa','libro','acta','folio','fecha','diploma','sede','asistencia')
	#list_filter=('programa','nombres')
	search_fields=['nombres','programa']

	resource_class = AlumnoResource
	
	

 
admin.site.register(Alumno,alumnoAdmin)
admin.site.register(Programa)
admin.site.register(userProfile)


