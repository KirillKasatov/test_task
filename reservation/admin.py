# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Order, Position


class PositionInline(admin.TabularInline):
    model = Position

class OrderAdmin(admin.ModelAdmin):
    inlines = [PositionInline]

admin.site.register(Order, OrderAdmin)