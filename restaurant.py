import math

class Table:
    def __init__(self, num_people):
        self.num_people = num_people
        self.bill = []

    def order(self, item, price, quantity = 1):
        menu_item = {"item": item, "price": price, "quantity": quantity}
        for i in self.bill:
            if i["item"] == item and i["price"] == price:
                i["quantity"] += quantity
                return 
        self.bill.append(menu_item)


    def remove(self, item, price, quantity):
        menu_item = {"item": item, "price": price, "quantity": quantity}
        for i in self.bill:
            if i["item"] == item and i["price"] == price:
                i["quantity"] -= quantity
                if i["quantity"] <= 0:
                    self.bill.remove(i)
                return True
        return False

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
        return math.ceil(self.get_subtotal() / self.num_people * 100) / 100
