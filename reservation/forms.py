# -*- coding: utf-8 -*-
from datetimewidget.widgets import DateWidget
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumbers import region_code_for_number

from reservation.models import Order, Position


class OrderForm(forms.ModelForm):
    class Meta(object):
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'address']

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if region_code_for_number(phone) != 'RU':
            raise forms.ValidationError(u'Неверный код страны')
        return phone


class PositionForm(forms.ModelForm):
    class Meta(object):
        model = Position
        fields = ('name', 'price', 'number')


class PositionFormset(
    forms.inlineformset_factory(Order, Position, form=PositionForm, max_num=3, can_delete=False, min_num=1)):
    pass


class OrdersFilterForm(forms.Form):
    dateTimeOptions = {
        'autoclose': 'true',
        'todayBtn': 'true',
    }
    date_from = forms.DateTimeField(widget=DateWidget(
        attrs={'id': "date_from"}, usel10n=True, bootstrap_version=3, options=dateTimeOptions
    ), required=False)
    date_to = forms.DateTimeField(widget=DateWidget(
        attrs={'id': "date_to"}, usel10n=True, bootstrap_version=3, options=dateTimeOptions
    ), required=False)

    phone_filter = PhoneNumberField(required=False)

    show_archive = forms.BooleanField(widget=forms.CheckboxInput, required=False)