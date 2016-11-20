from django.contrib import admin
from .models import usuario,pregunta
# Register your models here.
@admin.register(usuario)
class usuario_admin(admin.ModelAdmin):
	list_display = ('id','mail','name','last',)

@admin.register(pregunta)
class pregunta_admin(admin.ModelAdmin):
	list_display = ('id','nombre','categoria','si','no','propietario')