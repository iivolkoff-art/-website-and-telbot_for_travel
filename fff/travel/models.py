from django.db import models

class Travel(models.Model):
    name = models.CharField('имя заказчика', max_length=100)
    mail = models.CharField('почта', max_length=50)
    phone_number = models.CharField('номер телефона', max_length=20)
    place_of_chill = models.CharField('место для отдыха', max_length=100)

    def __str__(self): #выводит имя в html
        return self.name

