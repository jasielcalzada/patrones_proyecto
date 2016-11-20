from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^$',index_view,name='index_view'),
	url(r'^login/$','django.contrib.auth.views.login',{'template_name':'voto/login.html'}, name='login'),
	url(r'^registro_de_usuarios/$',signup.as_view(),name='registro_de_usuarios'),
	url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
	url(r'^hacer_pregunta/$',hacer_pregunta.as_view(),name='hacer_pregunta'),

]