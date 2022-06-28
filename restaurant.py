class Table:


    def __init__(self, number):
        self.number = number
        self.bill = []

    def order(self, item, price, quantity = 1):

        order_item = {
            'item': item,
            'price': price,
            'quantity': quantity, }

        if order_item.get('item') == item:
            order_item['quantity'] += 1
            self.bill.append(order_item)
        else:
            self.bill.append(order_item)

    # def remove(self, item, price, quantity=0):
    #     if item in self.bill:
    #         self.bill['quantity'] -= 1
    #         return True
    #     else:
    #         return False

    def remove(self, item, price, quantity=1):
        for items in self.bill:
            if items["item"] == item and items["price"] == price:
                if items["quantity"] - quantity == 0:
                    self.bill.remove(bills)
                elif items["quantity"] - quantity < 0:
                    return False
                else:
                    items["quantity"] -= quantity
                return True
        else:
            return False

    def get_subtotal(self):
        total_cost = 0
        for i in self.bill:
            total_cost += i['quantity'] * i['price']
        return total_cost

    def split(self):
        return round(self.get_subtotal()/self.number, 2)

    def get_total(self, service_charge: float = 0.1):
        total_dic = {
            'sub total' : '',
            'service charge' : '',
            'total': ''
        }

        sub_total = self.get_subtotal()
        total_service_charge = round(sub_total * service_charge, 2)
        total = sub_total + total_service_charge

        total_dic['sub total'] = '£' + str(sub_total)+str(0)
        total_dic['service charge'] = '£' + str(total_service_charge)
        total_dic['total'] = '£' + str(round(total, 2))










