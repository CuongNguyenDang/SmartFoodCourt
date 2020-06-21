
class Customer:
    def __init__(self,mode):
        self.mode = mode
    def order(self):
        return 0
    def pay(self,cusID,orderID,mode):
        return 0

class Account(Customer):
    def __init__(self,id,usename,password,name,level):
        self.id = id
        self.usename = usename
        self.password = password
        self.name = name
        self.level = level
        self.change = 0
    #overload
    def pay(self,total):
        return 0
    def recharge(self, money):
        return 0
#Duy's part_____________________________________
class FoodOrder:
    def __init__(self,orderID,cusname,name=None, quantity=None, state=None):
        self.orderID = orderID
        self.cusname = cusname
        self.name=[]
        self.quantity=[]
        self.state=[]
    def addFood(self,name,quantity,state):
        self.name.append(name)
        self.quantity.append(quantity)
        self.state.append(state)
    def deleteFood(self,name):
        i=0
        for x in self.name:
            if x==name:
                self.quantity[i]=0
                self.state[i] ="Da xoa"
            i+=1
#Enn Duy's part__________________________________

