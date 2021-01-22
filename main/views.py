from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, BookStore

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

def bookStore(request):
    book_list = BookStore.objects.all()
    return render(request, 'bookStore.html', {"book_list": book_list}) 

def book(request):
    book_list = BookStore.objects.all()
    return render(request, 'books.html', {"book_list": book_list}) 

def add_book(request):
    form = request.POST
    title = form['book_заголовок']
    subtitle = form['book_подзаголовок']
    description = form['book_описание']
    author = form['book_автор']
    genre = form['book_жанр']
    year = form['book_год']
    price = form['book_цена']
    return HttpResponse('Форма получена')   
   
 