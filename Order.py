import OrderCore as OC
class Order(OC.OrderCore):
    def __init__(self, OrderId, Username, SecurityId, price, quantity, isBuySide):
        # PROPERTIES
        super().__init__(OrderId, Username, SecurityId)
        self.Price = price
        self.IsBuySide = isBuySide
        self.InitialQuantity = quantity
        self.CurrentQuantity = quantity
    
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