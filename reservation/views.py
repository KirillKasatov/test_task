# -*- coding: utf-8 -*-
import datetime
from django.http import HttpResponseRedirect

from django.shortcuts import render, get_object_or_404, redirect, resolve_url

from reservation.forms import OrderForm, PositionFormset, OrdersFilterForm
from reservation.models import Order, OrderView
from reservation.tables import OrderTable


def index(request):
    orders = OrderView.objects.order_by('-creation_date')
    filter_form = OrdersFilterForm(request.GET)
    if filter_form.is_valid():
        show_archive = filter_form.cleaned_data['show_archive']
        date_from = filter_form.cleaned_data['date_from']
        date_to = filter_form.cleaned_data['date_to']
        phone_filter = filter_form.cleaned_data['phone_filter']
        if not show_archive:
            orders = orders.filter(is_archive=False)

        if date_from:
            orders = orders.filter(creation_date__date__gte=date_from)

        if date_to:
            orders = orders.filter(creation_date__date__lte=date_to)

        if phone_filter:
            orders = orders.filter(phone=phone_filter)

    table = OrderTable(orders, request=request)
    table.template = 'reservation/orders_table.html'
    return render(request, 'reservation/index.html', {
        'table': table,
        'filter_form': filter_form,
        'orders': orders
    })


def order(request, order=None):
    if order:
        order = get_object_or_404(Order, id=order)
    form = OrderForm(request.POST or None, instance=order)
    position_formset = PositionFormset(request.POST or None, instance=order)

    if form.is_valid() and position_formset.is_valid():
        position_formset.instance = form.save(commit=False)
        if order and (form.has_changed() or position_formset.has_changed()):
            position_formset.instance.change_date = datetime.datetime.now()
        position_formset.instance.save()
        position_formset.save()
        return redirect('index')
    return render(request, 'reservation/order.html', {
        'form': form, 'position_formset': position_formset
    })


def archive_order(request, order):
    order = get_object_or_404(Order, id=order)
    order.is_archive = not order.is_archive
    order.save()
    return HttpResponseRedirect(resolve_url('index')+'?'+request.GET.urlencode())