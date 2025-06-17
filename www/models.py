from datetime import timezone
from django.db import models


class Drink(models.Model):
    CATEGORY_CHOISES = [
        ('hot', 'Горячее'),
        ('cold', 'Холодное'),
        ('seasonal', 'Сезонное'),
        ('not', 'Неопределенно'),
    ]

    title = models.CharField(max_length=100)
    composition = models.TextField()
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='menu/')
    category = models.CharField(max_length=100, choices=CATEGORY_CHOISES, default='not')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Напиток'
        verbose_name_plural = 'Напитки'


class Poster(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateField()
    image = models.ImageField(upload_to='date/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мероприятиe'
        verbose_name_plural = 'Мероприятия'
