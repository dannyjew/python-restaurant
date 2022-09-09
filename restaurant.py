class Table:

    def __init__(self, dishes: int =1):
        self.dishes = dishes
        self.bill = []  # initially we don't have any dishes on our bill
        # bill is: number of dishes, item name, item price and quantity of given dish

    def order(self, item, price, quantity = 1):  # item, price, quantity
        if item in self.bill:
            self.bill.append({'item': item, 'price': price, 'quantity': quantity})
        else:
            self.bill.append({'item': item, 'price': price, 'quantity': quantity})

        return self.bill

    def remove(self, item, price, quantity):
        for orders in self.bill:
            if orders['item'] == item and orders['price'] == price:
                if orders['quantity'] >= quantity:
                    orders['quantity'] -= quantity
                    if orders['quantity'] == 0:
                        del orders['item']
                        del orders['price']
                        del orders['quantity']
                else:
                    return False # quantity is > quantity of the items on a bill
            else:
                return False
        return self.bill

    def get_subtotal(self):
        subtotal = 0
        for orders in self.bill:
            subtotal += (orders['price'] * orders['quantity'])
        return round(subtotal, 2)

    def get_total(self, service_charge=0.1):
        subtotal = format(self.get_subtotal(), '.2f')
        total = format(self.get_subtotal() * (1 + service_charge), '.2f')
        service = format(self.get_subtotal() * service_charge, '.2f')
        return {'Sub Total': f"£{subtotal}", 'Service Charge': f"£{service}", 'Total': f"£{total}"}


    def split_bill(self):
        subtotal_cost = round((self.get_subtotal()/self.dishes), 2)
        return subtotal_cost
