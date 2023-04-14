import OrderCore as OC
import CancelOrder as CO
import Order as order
class ModifyOrder(OC.OrderCore):
    def __init__(self, OrderId, Username, SecurityId, modifyPrice, modifyQuantity, isBuySide):
        # PROPERTIES
        super().__init__(OrderId, Username, SecurityId)
        self.ModifyPrice = modifyPrice
        self.Quantity = modifyQuantity
        self.IsBuySide = isBuySide

    def ToCancelOrder(self):
        CancelOrder = CO.CancelOrder(self)
        return CancelOrder
    
    def ToNewOrder(self):
        NewOrder = order.Order(self)
        return NewOrder