#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.prices = []
        self.discount = discount
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        self.last_transaction = price * quantity
        self.total += self.last_transaction
        self.items.append({'item': title, 'quantity': quantity})
        self.prices.append(price * quantity)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100.0) * self.total
            self.total -= discount_amount
            return f"After the discount, the total comes to ${self.total}."
        else:
            return "There is no discount to apply."

    def void_last_transaction(self):
        if self.prices:
            self.total -= self.last_transaction
            self.items.pop()
            self.prices.pop()
        else:
            self.total = 0

    def get_items(self):
      items_list = []
      for item in self.items:
        items_list.extend([item['item']] * item['quantity'])
      return items_list


    def get_items_with_quantity(self):
        return self.items
pass

