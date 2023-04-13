import IOrderCore as IOC
class OrderCore(IOC.IOrderCore):
    def __init__(self, OrderId, Username, SecurityId):
        self.OrderId = OrderId
        self.Username = Username
        self.SecurityId = SecurityId