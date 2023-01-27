import math
class Table:
    def __init__(self, num_of_people):
        self.num_of_people = num_of_people
        self.bill = []

    def order(self, item, price, quantity=1):
        table_order = {"item": item, "price": price, "quantity": quantity}
        for items in self.bill:
            if items["item"] == item and items["price"] == price:
                items["quantity"] += quantity
                return
        self.bill.append(table_order)

            #else:
            #   return self.bill.append(table_order)


    def remove(self, item, price, quantity=1):
        table_order = {"item": item, "price": price, "quantity": quantity}
        for items in self.bill:
            if items["item"] == item and items["price"] == price:
                items["quantity"] -= quantity
                if items["quantity"] <= 0:
                    self.bill.remove[items]
                return
        self.bill.append(table_order)

    def get_subtotal(self):
        subtotal = 0
        for i in self.bill:
            subtotal += i["price"] * i["quantity"]
        return subtotal

    def get_total(self, service_charge=0.1):
        subtotal = self.get_subtotal()
        service_charge_amount = subtotal * service_charge
        total = subtotal + service_charge_amount
        return {"Sub Total": "£{:.2f}".format(subtotal),
                "Service Charge": "£{:.2f}".format(service_charge_amount),
                "Total": "£{:.2f}".format(total)}

    def split_bill(self):
        return math.ceil(self.get_subtotal() / self.num_of_people * 100) / 100
