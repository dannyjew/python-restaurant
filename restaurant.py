class Table:
    def __init__(self,no_of_people:int):
        self.no_of_people = no_of_people
        self.bill = []
        
    def order(self, item:str, price:float, quantity:int=1):
        for order in self.bill:
            if item in order.values(): #if item is in bill adds up the quantity
                order['quantity']+=quantity
                print('Quantity of the order updated!', self.bill)
                return None
            continue
        self.bill.append({'item':item, 'price':price,'quantity':quantity})
        print('New item order appended!')

    def remove(self,item:str,price:float,quantity:int=1):
        for order in self.bill:
            if item in order.values() and price in order.values() and order['quantity']>=quantity: #if item is in bill and quantity passed is less than the order quantity
                order['quantity'] -= quantity
                if order['quantity'] == 0: #if quantity becomes 0
                    self.bill.remove(order)
                return True
        return False

    def get_subtotal(self):
        subtotal = 0
        for order in self.bill:
            subtotal += (order['price']*order['quantity'])
        return subtotal

    def get_total(self, service_charge:float=0.10):
        total = {'Sub Total':0, 'Service Charge':0, 'Total':0}
        subtotal =self.get_subtotal()
        service_charge = service_charge*subtotal
        # String representations in British pounds and pence.
        total['Sub Total'] = f'£{subtotal:,.2f}' 
        total['Service Charge'] = f'£{service_charge:,.2f}'
        total['Total'] = f'£{subtotal+service_charge:,.2f}'
        return total
    
    def split_bill(self):
        return round(self.get_subtotal()/self.no_of_people,2) # returns as a float as requested
