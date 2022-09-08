class Table:
    def __init__(self, no_of_people: int):
        self.bill = []
        self.no_of_people = no_of_people

    def order(self, item: str, price: float, quantity: int = 1):
        index = [
            i for i, itm in enumerate(self.bill)
            if itm["item"] == item
        ]
        if index:
            self.bill[index[0]]["quantity"] += quantity
        else:
            self.bill.append({
                "item": item,
                "price": price,
                "quantity": quantity
            })

    def remove(self, item: str, price: float, quantity: int = 1):
        product = [
            (i, itm) for i, itm in enumerate(self.bill)
            if itm["item"] == item and itm["quantity"] >= quantity and itm["price"] == price
        ]
        if product:
            i, itm = product[0]
            if itm["quantity"] > quantity:
                self.bill[i]["quantity"] -= quantity
            else:
                self.bill.pop(i)
            return True
        else:
            return False

    def get_subtotal(self):
        return sum([it["price"] * it["quantity"] for it in self.bill])

    def get_total(self, service_charge: float = 0.1):
        sub = self.get_subtotal()
        print()
        return {
            "Sub Total": "£" + "{:.2f}".format(round(sub, 2)),
            "Service Charge": "£" + str("{:.2f}".format(service_charge * sub)),
            "Total": "£" + str("{:.2f}".format(round((1 + service_charge) * sub, 2)))
        }

    def split_bill(self):
        return round(self.get_subtotal() / self.no_of_people, 2)
