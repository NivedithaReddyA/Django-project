from django.contrib import admin
from myapp.models import Employe
# Register your models here.
class EmployeAdmin(admin.modelAdmin):
    l=['number','name','salary']
admin.site.register(Employe,EmployeAdmin)