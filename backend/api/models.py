from django.db import models


class Item(models.Model):
    name = models.CharField('Имя', max_length=50)
    description = models.CharField('Описание', max_length=250)
    price = models.PositiveIntegerField('Стоимость')

    class Meta:
        ordering = ['-name']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Order(models.Model):
    items = models.ManyToManyField(Item, verbose_name='Товары')

    class Meta:
        ordering = ['-pk']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
