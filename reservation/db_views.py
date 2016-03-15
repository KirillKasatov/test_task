# -*- coding: utf-8 -*-
from django.db import connection


def create_orders_view(**kwargs):
    print '  (re)creating orders_view...'

    sql = """CREATE OR REPLACE VIEW orders_view AS
 SELECT reservation_order.id,
    reservation_order.first_name,
    reservation_order.last_name,
    reservation_order.phone,
    reservation_order.address,
    reservation_order.creation_date,
    reservation_order.change_date,
    reservation_order.is_archive,
    sum(reservation_position.price * reservation_position.number::numeric) AS total_price
   FROM reservation_order
     LEFT JOIN reservation_position ON reservation_order.id = reservation_position.order_id
  GROUP BY reservation_order.id
  ORDER BY reservation_order.id
  """

    cursor = connection.cursor()
    cursor.execute(sql)
    print '  Done creating orders_view.'