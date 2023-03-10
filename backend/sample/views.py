from django.shortcuts import render

from .models import *

def index(request):
	todos = Todo.objects.all()
	return render(request, 'sample/index.html', {
		'todos': todos
		})