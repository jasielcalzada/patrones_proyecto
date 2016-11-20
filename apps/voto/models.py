from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator,MaxValueValidator
from django.utils import timezone
import datetime
import time

# Create your models here.
class usuario(models.Model):
	user_perfil = models.OneToOneField(User, related_name="profile")
	mail = models.EmailField()
	name = models.CharField(max_length=64)
	last = models.CharField(max_length=64)

	def __unicode__(self):
		return '%s'%(self.id)


class pregunta(models.Model):
	nombre = models.CharField(max_length=64)
	categoria = models.CharField(max_length=64)
	si = models.BooleanField(default=False,blank=True)
	no = models.BooleanField(default=False,blank=True)
	propietario = models.ForeignKey(usuario,related_name='usuarion',null=True,blank=True,)

	def __unicode__(self):
		return '%s'%(self.id)


