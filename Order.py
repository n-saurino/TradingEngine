import OrderCore as OC
class Order(OC.OrderCore):
    '''
    def __init__(self, OrderId, Username, SecurityId, price, quantity, isBuySide):
        # PROPERTIES
        super().__init__(OrderId, Username, SecurityId)
        self.Price = price
        self.IsBuySide = isBuySide
        self.InitialQuantity = quantity
        self.CurrentQuantity = quantity
    '''

    def __init__(self, *args):
        # PROPERTIES
        if len(args) == 6:
            super().__init__(args[0], args[1], args[2])
            self.Price = args[3]
            self.IsBuySide = args[5]
            self.InitialQuantity = args[4]
            self.CurrentQuantity = args[4]

        if len(args) == 4:
            # PROPERTIES
            # arg[0] = ModifyOrder Object
            # arg[1] = Price
            # arg[2] = Quantity
            # arg[3] = IsBuySide
            super().__init__(args[0].OrderId, args[0].Username, args[0].SecurityId)
            self.Price = args[1]
            self.IsBuySide = args[3]
            self.InitialQuantity = args[2]
            self.CurrentQuantity = args[2]

    # METHODS
    def IncreaseQuantity(self, quantityDelta):
        self.CurrentQuantity += quantityDelta

    def DecreaseQuantity(self, quantityDelta):
        self.CurrentQuantity -= quantityDelta

    def Display(self):
        print(self.OrderId, self.Price, self.CurrentQuantity, self.IsBuySide)


def main():
    test_order = Order(1, "nsaurino", 1111, 157.50, 100, True)
    print("Object Created")
    test_order.IncreaseQuantity(50)
    test_order.Display()

if __name__ == "__main__":
    main()