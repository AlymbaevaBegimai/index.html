from django.db import models

#переведие полей задач

class ToDo(models.Model): #models предоставил сам django
    text = models.CharField(max_length=100) #текст самой задачи # максимальная длина=100 символов
    created_at = models.DateTimeField(auto_now_add=True) #атрибут позволит дату создания создавать самому сайту
    is_closed = models.BooleanField(default=False)  #по умолчанию задача не помечена
    is_favorite = models.BooleanField(default=False) 
    

class BookStore(models.Model):
    title = models.CharField( max_length=100, name='заголовок')
    subtitle = models.CharField(max_length=80, name='подзаголовок')
    description = models.CharField(max_length=700,name='описание')
    price = models.IntegerField(name='цена')
    genre = models.CharField(max_length=50,name='жанр')
    author = models.CharField(max_length=50,name='автор')
    year = models.DateField(max_length=50,name='год')
    date = models.DateField(auto_now_add=50,name='дата')  