# -*- coding: utf-8 -*-
import re
from django.template.defaultfilters import yesno
from django_tables2 import tables, columns, A
from reservation.models import OrderView


class GetSafeLinkColumn(columns.LinkColumn):
    def compose_url(self, record, *args, **kwargs):
        column = args[0]
        return super(GetSafeLinkColumn, self).compose_url(record, *args, **kwargs) + '?' + column.table.request.GET.urlencode()


class OrderTable(tables.Table):
    full_name = columns.Column(verbose_name=u"Полное имя", order_by=('first_name', 'last_name'))
    is_archive = GetSafeLinkColumn('archive_order', verbose_name=u"", args=[A('pk')],
                                    text=lambda v: yesno(v.is_archive, u'Достать из архива,В архив'), orderable=False)

    edit = columns.LinkColumn('change_order', empty_values=(), verbose_name=u"", args=[A('pk')], text=u'Ред.',
                              orderable=False)

    def __init__(self, *args, **kwargs):
        self.request = kwargs['request']
        super(OrderTable, self).__init__(*args, **kwargs)

    def render_phone(self, value):
        value = str(value)
        return '%s (%s) %s-%s-%s' % (value[:2], value[2:5], value[5:8], value[8:10], value[10:12])

    class Meta:
        model = OrderView
        per_page = 20
        attrs = {'id': 'orders-table', }
        fields = sequence = (
            'creation_date', 'change_date', 'phone', 'full_name', 'address', 'total_price', 'edit', 'is_archive')