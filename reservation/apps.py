from __future__ import unicode_literals

from django.apps import AppConfig
from django.db.models.signals import post_migrate
from reservation.db_views import create_orders_view


class ReservationConfig(AppConfig):
    name = 'reservation'

    def ready(self):
        post_migrate.connect(create_orders_view, sender=self)