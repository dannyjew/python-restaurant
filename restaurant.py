class Table:

    def __init__(self,Number_of_people):
        self.number_of_people = Number_of_people
        self.bill = []

    def order(self, item: str, price:float, quantity:int=1):
        for order in self.bill:
            if item in order.values():
                order["quantity"] += quantity
            continue
        self.bill.append({"item":item,"price":price,"quantity":quantity})



    def remove(self, item: str, price:float, quantity:int=1):
        for order in self.bill:
            if item in order.values() and price in order.values():
                if quantity < order["quantity"]:
                    order["quantity"] -= quantity
                else:
                    self.bill.remove(order)
                return True
            return False

    def get_subtotal(self):
        sub_total=0
        for order in self.bill:
            sub_total += order["price"]*order["quantity"]
        return sub_total

    def get_total(self, service_charge : float = 0.1):
        total = {"Sub Total":0, "Service Charge": 0, "Total": 0}
        subtotal = self.get_subtotal()
        service_charge = service_charge * subtotal
        total ["Sub Total"] = f'£{subtotal:,.2f}'
        total ["Service Charge"] = f'£{service_charge:,.2f}'
        total ["Total"] = f'£{subtotal+service_charge:,.2f}'
        return total

    def split_bill(self):
        return round(self.get_subtotal() / self.number_of_people, 2)


