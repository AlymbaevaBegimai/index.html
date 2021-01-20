from django.db import models

#переведие полей задач

class ToDo(models.Model): #models предоставил сам django
    text = models.CharField(max_length=100) #текст самой задачи # максимальная длина=100 символов
    created_at = models.DateTimeField(auto_now_add=True) #атрибут позволит дату создания создавать самому сайту
    is_closed = models.BooleanField(default=False)  #по умолчанию задача не помечена
    is_favorite = models.BooleanField(default=False) 
    

