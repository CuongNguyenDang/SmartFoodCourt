import uuid
from flask_mysqldb import MySQL
import MySQLdb
import model.stall, model.cart

mysql = MySQLdb.connect(host = 'sql12.freemysqlhosting.net', user = 'sql12358320', passwd = 'PqvDtHlTSL', db = 'sql12358320', charset = 'utf8')
cur = mysql.cursor(MySQLdb.cursors.DictCursor)

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

class Bill:
    def __init__(self,foods = []):
        self.id = str(uuid.uuid1())
        self.foods = foods
        self.cost = 2000

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
#End Duy's part__________________________________


#stall
cur.execute("SELECT * FROM food")
tmp = cur.fetchall()

food_list = model.stall.FoodList(None)
for t in tmp:
    food = model.stall.Food(t['id'],t['name'],t['stall_id'],t['image'],t['cost'],t['status'])
    food_list.push(food)

cur.execute("SELECT * FROM stall")
tmp = cur.fetchall()
stall_list = model.stall.StallList(None)
for t in tmp:
    stall = model.stall.Stall(t['id'],t['name'],t['image'],t['status'])
    stall_list.push(stall)
    foodID = t['food'].split(',')
    for f in foodID:
        tmp2 = food_list.findbyID(int(f))
        if tmp2 is not None:
            stall.addfood(tmp2)

#cart
cart = model.cart.Cart()

#Nam's Class_____________________
class StallInfo:
    def __init__(self,cur,stallid,date,stall_list):
        cur.execute("SELECT * FROM report WHERE stall_id="+str(stallid)+" and date='"+date+"'")
        tmp = cur.fetchone()
        if tmp is not None:
            tmp2 = tmp['food'].split(',')
            ID = 0
            num = 0
            for t in tmp2:
                if int(t.split('-')[1])>num:
                    ID = int(t.split('-')[0])
                    num = int(t.split('-')[1])
            food = None
            stall = stall_list.findbyID(stallid)
            for f in stall.foodlist:
                if f.foodID == ID:
                    food = f
            self.stallid = stallid
            self.name = stall.name
            self.date = date
            self.payment = tmp['payment']
            self.pager = tmp['pager']
            self.bestseller = food.name
        else:
            self.stallid = None
#__________________end Nam's Class
