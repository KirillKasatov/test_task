# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


class AbstractOrder(models.Model):
    first_name = models.CharField(u'Имя', max_length=100)
    last_name = models.CharField(u'Фамилия', max_length=100)
    phone = PhoneNumberField(u'Номер телефона')
    address = models.TextField(u'Адрес', )
    creation_date = models.DateTimeField(u'Дата создания', auto_created=True, auto_now_add=True)
    change_date = models.DateTimeField(u'Дата изменения', null=True)
    is_archive = models.BooleanField(u'В архиве', default=False)

    class Meta(object):
        abstract = True

    @property
    def full_name(self):
        return ' '.join([self.first_name.capitalize(), self.last_name.capitalize()])

    def total_price(self):
        total = 0
        for p in self.positions.all():
            total += p.price * p.number
        return total

    def __unicode__(self):
        return self.first_name


class Order(AbstractOrder):
    pass


class OrderView(AbstractOrder):
    total_price = models.DecimalField(u'Общая стоимость', max_digits=15, decimal_places=2)

    class Meta(object):
        managed = False
        db_table = 'orders_view'


class Position(models.Model):
    name = models.CharField(u'Наименование', max_length=250)
    price = models.DecimalField(u'Цена', max_digits=15, decimal_places=2)
    number = models.IntegerField(u'Количество', )
    order = models.ForeignKey(Order, related_name='positions')