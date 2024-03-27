#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transactions = []

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        
        for i in range(quantity):
            self.items.append(item)

        self.last_transactions.append({"item": item, "quantity": quantity, "price": price})

    def apply_discount(self):
        if not self.discount:
            print("There is no discount to apply.")
        else:
            discount_given  = int((self.total * self.discount) / 100)
            self.total = self.total - discount_given

            print("After the discount, the total comes to ${}.".format(self.total))

    def void_last_transaction(self):
        if not self.last_transactions:
            return "There are no transactions to void."

        self.total -= (self.last_transactions[-1]["price"] * self.last_transactions[-1]["quantity"])

        for i in range(self.last_transactions[-1]["quantity"]):
            self.items.pop()

        self.last_transactions.pop()
