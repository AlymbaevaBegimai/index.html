from django.shortcuts import render, HttpResponse, redirect
from .models import *

def homepage(request):
    return render(request, 'index.html')

def second(request):
    return HttpResponse('test 2 page')  

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, 'test.html',{'todo_list':todo_list})  



def add_todo(request):
    form = request.POST 
    text = form['todo_text'] #получаем значение списка (текст)
    todo = ToDo(text=text) #создали объект класса и прописали атрибуты 
    todo.save() #отправить запрос на БД, для того,чтобы сохранить задачу в базу
    #print(text)
    #print(form)   
    #return HttpResponse('Форма получена')   
    return redirect(test) 

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test) 

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test) 

def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)  

def close_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed               #True
    todo.save()
    return redirect(test)

def add (request):
    return HttpResponse("book") 
