class Table:

    def __init__(self, number_of_people):
        self.number_of_people = number_of_people
        self.bill = []

    def order(self, item, price, quantity=1):
        dict_bill = {"item": item, "price": price, "quantity": quantity}
        for item in self.bill:
            if item['item'] == dict_bill['item'] and item['price'] == dict_bill['price']:
                item['quantity'] += dict_bill['quantity']
                return
        self.bill.append(dict_bill)
        return self.bill

    def remove(self, item, price, quantity=1):
        dict_bill = {"item": item, "price": price, "quantity": quantity}
        for item in self.bill:
            if item['item'] == dict_bill['item'] and item['price'] == dict_bill['price']and item['quantity'] >= dict_bill['quantity']:
                item['quantity'] -= dict_bill['quantity']
                if item['quantity'] == 0 :
                    self.bill.remove(item)
                return True
        return False

    def get_subtotal(self):
        subtotal = 0
        for i in self.bill:
            subtotal += i["price"] * i["quantity"]
        return subtotal

    def get_total(self, service_charge=0.1):

        total_bill = {"Sub Total": self.get_subtotal(), "Service Charge": 0, "Total": 0}

        total_bill["Sub Total"] = f"£{self.get_subtotal():,.2f}"
        total_bill["Service Charge"] = f"£{ self.get_subtotal() * service_charge :,.2f}"
        total_bill["Total"] = f"£{self.get_subtotal() + self.get_subtotal() * service_charge:,.2f}"

        return total_bill

    def split_bill(self):

        subtotal_2 = self.get_subtotal()
        the_split_bill = self.get_subtotal()/self.number_of_people

        return round(the_split_bill, 2)

if __name__ == "__main__":
    a = Table(6)
    a.order('lobster',53,1)
    a.order('lobster', 53)
    a.order('ice-cream', 6,4)
    a.remove("lobster", 53,1)
    print("The updated order is ", a.bill)

    print("The subtotal is £"+str(a.get_subtotal()))
    print(a.get_total())
    print("The subtotal cost per person comes down to £" + str(a.split_bill()))