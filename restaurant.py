class Table:
    def __init__(self, no_of_people: int):
        self.bill = []
        self.no_of_people = no_of_people

    def order(self, item: str, price: float, quantity: int = 1):
        # Check if there is an item in the self.bill list that has a matching item name and price to the given one.
        # The list should either be empty (if no matches present) or have one item in it
        index = [
            i for i, itm in enumerate(self.bill)
            if itm["item"] == item
        ]

        # Add given quantity to the existing one if the list isn't empty - i.e. of a matching item-price pair was found.
        # If no matching items, append a dictionary to the list with order details.
        if index:
            self.bill[index[0]]["quantity"] += quantity
        else:
            self.bill.append({
                "item": item,
                "price": price,
                "quantity": quantity
            })

    def remove(self, item: str, price: float, quantity: int = 1):
        # Check if there is an item in the self.bill list that has a matching item name and price to the given one.
        # The list should either be empty (if no matches present) or have the index of the item and its quantity
        # enclosed in a tuple.
        product = [
            (i, itm["quantity"]) for i, itm in enumerate(self.bill)
            if itm["item"] == item and itm["price"] == price
        ]

        # i.e. "if the list product is not empty"
        if product:
            # Unpack the item index and its quantity from the list-tuple wrapping
            i, qty = product[0]
            # Consider three cases where quantity of the item already in the list is:
            # 1. Greater than the quantity that user wants to subtract:
            #    --->   get the difference of quantities
            # 2. Equal the quantity that user wants to subtract:
            #    --->   remove the item from the list
            # 3. Smaller than the quantity that user wants to subtract:
            #    --->   return False as the operation cannot be completed
            if qty > quantity:
                self.bill[i]["quantity"] -= quantity
            elif qty == quantity:
                self.bill.pop(i)
            return bool(product) and (qty >= quantity)
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
