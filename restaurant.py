class Table:

    def __init__(self, Number_of_people):
        self.Number_of_people = Number_of_people
        self.bill = []

    def order(self, item: str, price: float, quantity: int = 1):
        for order in self.bill:
            if order["item"] == item and order["price"] == price:
                order["quantity"] += quantity
                print("quantity updated", self.bill)
                return None
            continue
        self.bill.append({"item": item, "price": price, "quantity": quantity})
        return self.bill

    def remove(self, item: str, price: float, quantity: int = 1):
        for order in self.bill:
            if order["item"] == item and order["price"] == price and order["quantity"] >= quantity:
                order["quantity"] -= quantity
                if order["quantity"] == 0:
                    self.bill.remove(order)
                return True
        return False

    def get_subtotal(self):
        subtotal = 0
        for item in self.bill:
            subtotal += (item['price'] * item['quantity'])
        return subtotal

    def get_total(self, service_charge=0.1):
        total = {"Sub Total": self.get_subtotal(), "service charge": service_charge, "Total": 0}
        total["Total"] = total["Sub Total"] * total["service charge"] + total["Sub Total"]
        total["service charge"] = total["Sub Total"] * total["service charge"]
        return total

    def split_bill(self):
        split = self.get_subtotal() / self.Number_of_people
        return round(split)
