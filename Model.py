import uuid


class Customer:
    def __init__(self, mode):
        self.mode = mode

    def order(self):
        return 0

    def pay(self, cusID, orderID, mode):
        return 0


class Account(Customer):
    def __init__(self, id, usename, password, name, level):
        self.id = id
        self.usename = usename
        self.password = password
        self.name = name
        self.level = level
        self.change = 0
    # overload

    def pay(self, total):
        return 0

    def recharge(self, money):
        return 0


class Bill:
    def __init__(self, foods=[]):
        self.id = str(uuid.uuid1())
        self.foods = foods
        self.cost = 2000
