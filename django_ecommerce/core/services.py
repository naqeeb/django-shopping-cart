from decimal import Decimal, ROUND_HALF_UP
import random

from core.models import Order


class CreateOrderService(object):
    def __init__(self, user, store):
        self.user = user
        self.store = store

    def create(self, order_total):
        order_number = self._generate_order_number()
        order = Order.objects.create(store=self.store,
                                    user=self.user,
                                    external_id=order_number,
                                    total=order_total,
                                    status=Order.STATUS_NEW)
        return order

    def _generate_order_number(self):
        return random.randint(100000, 900000)


class CalculateOrderItemService(object):
    def __init__(self, item):
        self.item = item

    def calculate(self):
        price = self.item.price
        quantity = self.item.quantity
        total = self._calculate_total(price, quantity)
        self._update_total(total)
        return total

    def _calculate_total(price, quantity):
        raw_total = price * quantity
        return Decimal(raw_total.quantize(Decimal('.01'), \
            rounding=ROUND_HALF_UP))

    def _update_total(self, total):
        self.item.total = total
        self.item.save()


class CalculateOrderService(object):
    def __init__(self, order, calc_item_total_cls=CalculateOrderItemService):
        self.order = order
        self.items = self.order.items
        self.calc_item_total_cls = calc_item_total_cls

    def calculate(self):
        total = self._calculate_total()
        self._update_total(total)

    def _calculate_total(self):
        order_total = Decimal(0.0)

        for item in self.items:
            calc_item_total = self.calc_item_total_cls(item)
            order_total += calc_item_total.calculate()
        return order_total

    def _update_total(self, total):
        self.order.total = total
        self.order.save()
