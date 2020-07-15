
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
status=["Chưa làm","Đang làm","Đã xong","Xóa"]
class OrderList:
    def __init__(self,order): 
        self.order=[]
        self.max=0
        if order is not None:
            order.orderID = self.max+1
            self.order.append(order)
            self.max=1
    def push(self, order):
        order.orderID = self.max+1
        self.max+=1
        self.order.append(order)
    def findbyName(self, name):
        result = []
        for ords in self.order:
            if ords.name == name:
                result.append(ords)
                return result
    def removeFood(self, ID,fID):
        for ords in self.order:
            if ords.orderID == ID:
                x=0
                while ords.food[x].foodID< ords.max:
                    if ords.food[x].foodID==fID:
                        a=x
                        while ords.food[a].foodID <ords.max:
                            ords.food[a]= ords.food[a+1]
                            a+=1
                        del ords.food[a]
                    x+=1
    def changestatus(self,ID,fID,foodstatus):
        i= int(foodstatus)
        def use0():
            return status[0]
        def use1():
            return status[1]
        def use2():
            return status[2]
        def use3():
            self.removeFood(ID,fID)
        switcher={
                0:use0,
                1:use1,
                2:use2,
                3:use3
            }
        for ords in self.order:
            if ords.orderID== ID:
                for f in ords.food:
                    if f.foodID== fID:
                        func= switcher.get(i)
                        if i!=3:
                            f.state=func()
                            print(f.state)
                        else:
                            func()
                return ords
    def clear(self):
        self.__init__(None)
class FoodOrder:
    def __init__(self,cusname,food):
        self.food=[]
        self.max=0
        if food is not None:
            food.foodID=1
            self.food.append(food)
            self.max = food.foodID
        self.name = cusname
        self.orderID=0
    def addFood(self,food):
        food.foodID= self.max+1
        self.max= food.foodID
        self.food.append(food)

class Food:
    def __init__(self,fname,quantity):
        self.name= fname
        self.quantity=quantity
        self.state= status[0]
        self.foodID=0
Foodlist =[["Gà",1],
      ["Vịt",2],
      ["Bò",1],
      ["Cá",2],
      ["Heo",1],
      ["Mì",2],
      ["Cơm",2],
      ["Hủ tiếu",1],
      ["Bún",1],
      ["Coca",1],
      ["Pepsi",2],
      ["7up",3]]

#customer1
or1=[Foodlist[1],Foodlist[3],Foodlist[5],Foodlist[7],Foodlist[9],Foodlist[11]]
ord1=FoodOrder("Phương Bảo Trân",None)
for food in or1:
    f=Food(food[0],food[1])
    ord1.addFood(f)
#customer2
or2=[Foodlist[0],Foodlist[2],Foodlist[4],Foodlist[6],Foodlist[8],Foodlist[10]]
ord2=FoodOrder("Lê Quang Duy",None) 
for food in or2:
    f=Food(food[0],food[1])
    ord2.addFood(f)
OrdList= OrderList(ord1)
OrdList.push(ord2)


#Enn Duy's part__________________________________

