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

def books(request):
    books = BookStore.objects.all()
    return render(request, 'bookStore.html', {'books':books}) 

def add_book(request):
    form = request.POST
    book = BookStore(
        title=form['title'],
        subtitle=form['subtitle'],
        description=form['description'],
        author=form['author'],
        genre=form['genre'],
        year=form['date'][:10],
        price=form['price']
    )

    book.save()

    return redirect(bookStore)  

    def delete_book(request, id):
        book = BookStore.objects.get(id=id)
        book.delete()
        return redirect(bookStore)  

    def mark_book(request, id):
        book = BookStore.objects.get(id=id)
        book.is_favorite = True
        book.save()
        return redirect(bookStore) 

    def unmark_book(request, id):
        book = BookStore.objects.get(id=id)
        book.is_favorite = False
        book.save()
        return redirect(bookStore) 

