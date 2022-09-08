class Table:
    def __init__(self, Number_of_people):
        self.number_of_people = Number_of_people
        self.bill = []


    def order(self, item, price, quantity = 1 ):

        for item1 in self.bill:
            if item1["item"] == item and item1["price"] == price:
                 item1["quantity"] += quantity
                 return None

        self.bill.append({"item": item, "price": price, "quantity": quantity})



    def remove(self, item, price, quantity = 1):
        for item2 in self.bill:
            if item2["item"] == item and item2["price"] == price:
                if item2["quantity"] - quantity <= 0:
                    return False
                else:
                    item2["quantity"] -= quantity
                    return True
            return False


    def get_subtotal(self):
        table_total = []
        for item in self.bill:
            table_total.append(item["price"] * item["quantity"])
        return sum(table_total)


    def get_total(self, service_charge : float = 0.1):
        return {'Sub Total': "£" + str(self.get_subtotal()), 'Service Charge': "£" + str((service_charge * self.get_subtotal())), 'Total': "£" + str((self.get_subtotal()) +(self.get_subtotal() * service_charge)) }

    def split_bill(self):
        test = self.get_total()
        return round(float(test['Sub Total'].lstrip("£")) / self.number_of_people, 2)



