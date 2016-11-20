from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.views.generic import FormView, CreateView, ListView,DetailView,UpdateView,DeleteView
from .forms import Userform
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from .models import usuario,pregunta
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from django.contrib.auth.models import User
# Create your views here.

def index_view(request):
	return render(request,'voto/index.html')

class signup(FormView):
	template_name='voto/signup.html'
	form_class = Userform
	success_url = reverse_lazy('index_view')

	def form_valid(self,form):
		user = form.save()
		p = usuario()
		p.user_perfil = user
		p.mail = form.cleaned_data['mail']
		p.name = form.cleaned_data['name']
		p.last = form.cleaned_data['last']
		p.save()
		return super(signup,self).form_valid(form)

class hacer_pregunta(CreateView):
	template_name = 'voto/pregunta.html'
	model = pregunta
	fields = ['nombre','categoria','si','no','propietario']
	success_url = reverse_lazy('index_view')

	def post(self, request, *args, **kwargs):
		flag = False
		p = pregunta()
		query = pregunta.objects.filter(nombre = request.POST['nombre'])
		if query:
			if query.count == 1:
				flag = False
		else:
			#user = usuario.objects.get(id= a)
			a = request.POST['propietario']
			user = usuario.objects.get(id=a)
			print user
			p.nombre = request.POST['nombre']
			p.categoria = request.POST['categoria']
			p.si = request.POST.get('si','')
			p.no = request.POST.get('no','')
			p.propietario = user
			p.save()
		return render(request,'voto/pregunta.html', {'flag':flag})



