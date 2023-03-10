from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from .models import *

def index(request):
	return render(request, 'sample/index.html', {})


def submit(request):
	if request.method == "POST":
		title = request.POST['title']
		new_todo = Todo(title=title)
		new_todo.save()
		return HttpResponse('Added New Todo')
		
	return render(request, 'sample/submit.html')


def getTodo(request):
	todos = Todo.objects.all()

	return JsonResponse({"todos":list(todos.values())})