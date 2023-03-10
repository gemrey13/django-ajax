from django.shortcuts import render
from django.http import JsonResponse

from .models import *

def index(request):
	return render(request, 'sample/index.html', {})

def getTodo(request):
	todos = Todo.objects.all()

	return JsonResponse({"todos":list(todos.values())})