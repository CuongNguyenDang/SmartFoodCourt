import uuid


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
        
#stall

class Food:
    def __init__(self, name, img, cost, status):
        self.name = name
        self.foodID = 0
        self.stallID = None
        self.img = img
        self.cost = cost
        self.status = status

class Stall:
    def __init__(self, name, img, status):
        self.name = name
        self.stallID = 0
        self.img = img
        self.foodlist = []
        self.status = status
        self.next = None
        self.min = 0
        self.max = 0

    def addfood(self, food):
        if not self.foodlist:
            self.min = food.cost
            self.max = food.cost
        else:
            for f in self.foodlist:
                if f.cost > self.max:
                    self.max = f.cost
                if f.cost < self.min:
                    self.min = f.cost
        food.stallID = self.stallID
        if self.foodlist is None:
            food.foodID = 1
        else:
            food.foodID = len(self.foodlist)+1
        self.foodlist.append(food)
        
class StallList:
    def __init__(self, stall):
        if stall is not None:
            stall.stallID = 1
        self.head = stall
        self.tail = stall

    def push(self, stall):
        if self.head is None:
            stall.stallID = 1
        else:
            stall.stallID = self.tail.stallID+1
        self.tail.next = stall
        self.tail = stall
    
    def findbyID(self, ID):
        tmp = self.head
        while tmp is not None:
            if tmp.stallID == ID:
                return tmp
            tmp = tmp.next
        return None

    def findfoodbyID(self, ID):
        tmp = self.findbyID(ID[0]).foodlist
        for f in tmp:
            if f.foodID == ID[1]:
                return f
        return None
    
    def findbyName(self, string):
        result = []
        tmp = self.head
        while tmp is not None:
            if string.lower() in tmp.name.lower():
                result.append(tmp)
            tmp = tmp.next
        return result
    
    def findfood(self, string):
        result = []
        tmp = self.head
        while tmp is not None:
            for f in tmp.foodlist:
                if string.lower() in f.name.lower():
                    dic = {"stall": tmp.name, "food": f}
                    result.append(dic)
            tmp = tmp.next
        return result

    def remove(self, ID):
        tmp = self.head
        if tmp.stallID == ID:
            self.head = tmp.next
            return
        while tmp is not None:
            if tmp.next.stallID == ID:
                tmp.next = tmp.next.next
                return

    def clear(self):
        self.__init__(None)

pizza = Food('Pizza','pizzahut/pizza.jpg',200,1)
spaghetti = Food('Mỳ Ý','pizzahut/spaghetti.jpg',80,1)
salad = Food('Salad trộn','pizzahut/salad.jpg',50,1)
pizzahut = Stall('Pizza Hut','pizzahut/pizzahut.jpg',1)
stalllist = StallList(pizzahut)
pizzahut.addfood(pizza)
pizzahut.addfood(spaghetti)
pizzahut.addfood(salad)

chicken = Food('Gà rán','kfc/ga.jpg',100,1)
hamburger = Food('Hamburger','kfc/hamburger.jpg',50,1)
rice = Food('Cơm','kfc/com.jpg',40,1)
kfc = Stall('KFC','kfc/kfc.jpg',1)
stalllist.push(kfc)
kfc.addfood(chicken)
kfc.addfood(hamburger)
kfc.addfood(rice)


#cart

class Cart:
    def __init__(self):
        self.list=[]
        self.count=[]

    def addtoCart(self,food):
        if food in self.list:
            self.count[self.list.index(food)]+=1
        else:
            self.list.append(food)
            self.count.append(1)

    def remove(self,food):
        self.count.pop(self.list.index(food))
        self.list.remove(food)

    def less(self,food):
        if self.count[self.list.index(food)]==1:
            self.remove(food)
        else:
            self.count[self.list.index(food)]-=1

    def cancel(self):
        self.list.clear()

cart = Cart()