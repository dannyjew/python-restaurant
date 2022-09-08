import math

class table:
    def __init__(self, Number_of_people):
        self.number_of_people = Number_of_people
        self.bill = []


    def order(self, order_dict : dict):
        if "quantity" not in order_dict:
            order_dict["quantity"] = 1
        elif order_dict["quantity"] <= 0:
            order_dict["quantity"] = 1

        for item in self.bill:
            if item["item"] == order_dict["item"] and item["price"] == order_dict["price"]:
                new_quantity = item["quantity"] + order_dict["quantity"]
                item["quantity"] = new_quantity

        self.bill.append(order_dict)



    def remove(self, order_dict : dict):
        for item in self.bill:
            if item["item"] == order_dict["item"] and item["price"] == order_dict["price"]:
                if item["quantity"] - order_dict["quantity"] <= 0:
                    return False
                else:
                    new_quantity = item["quantity"] - order_dict["quantity"]
                    item["quantity"] = new_quantity
                    return self.bill
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


t = table(6)
t.order({"item" : "food1", "price" : 20, "quantity" : 3})
t.order({"item" : "food2", "price" : 10, "quantity" : 1})
t.order({"item" : "food3", "price" : 3.2, "quantity" : 1})


print(t.get_total(0.15))
print(t.split_bill())

