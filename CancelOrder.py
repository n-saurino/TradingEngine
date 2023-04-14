import OrderCore as OC
class CancelOrder(OC.OrderCore):
    def __init__(self, OrderId, Username, SecurityId):
        super().__init__(OrderId, Username, SecurityId)
        
