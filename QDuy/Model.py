
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
Foodlist =[["Gà",1,"Chưa làm"],
      ["Vịt",2,"Chưa làm"],
      ["Bò",1,"Chưa làm"],
      ["Cá",2,"Chưa làm"],
      ["Heo",1,"Chưa làm"],
      ["Mì",2,"Chưa làm"],
      ["Cơm",2,"Chưa làm"],
      ["Hủ tiếu",1,"Chưa làm"],
      ["Bún",1,"Chưa làm"],
      ["Coca",1,"Chưa làm"],
      ["Pepsi",2,"Chưa làm"],
      ["7up",3,"Chưa làm"]]
OrdList={}
OrdList["orderID"]=["0001","0002"]
OrdList["cusname"]=["Phương Bảo Trân","Lê Quang Duy"]
#customer1
or1=[Foodlist[1],Foodlist[3],Foodlist[5],Foodlist[7],Foodlist[9],Foodlist[11]]
ord1=FoodOrder("0001","Phương Bảo Trân") 
for food in or1:
    ord1.addFood(food[0],food[1],food[2])
#customer2
or2=[Foodlist[0],Foodlist[2],Foodlist[4],Foodlist[6],Foodlist[8],Foodlist[10]]
ord2=FoodOrder("0002","Lê Quang Duy") 
for food in or2:
    ord2.addFood(food[0],food[1],food[2])
OrdList=[ord1,ord2]
status={"state0":"Chưa làm",
        "state1" :"Đang làm",
        "state2":"Đã xong",
        "state3":"Đã xóa"}
#Enn Duy's part__________________________________

