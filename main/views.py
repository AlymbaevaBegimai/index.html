from django.shortcuts import render, HttpResponse
from .models import ToDo

def homepage(request):
    return render(request, 'index.html')


def test(request):
    return render(request, 'test.html') 

def second(request):
    return HttpResponse('test 2 page')  

def create(request):
    return render(request, 'create.html')


def update(request):
    return render(request, 'update.html')


def delete(request):
    return render(request, 'delete.html')