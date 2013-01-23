from django.contrib import admin
from cuadros.models import cuadros

class cuadrosAdmin(admin.ModelAdmin):
	pass

admin.site.register(cuadros, cuadrosAdmin)