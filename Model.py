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
    def __init__(self, name, ID, stallID, img, cost, status):
        self.name = name
        self.foodID = ID
        self.stallID = stallID
        self.img = img
        self.cost = cost
        self.status = status

class Stall:
    def __init__(self, name, ID, img, foodlist, status):
        self.name = name
        self.stallID = ID
        self.img = img
        self.foodlist = foodlist
        self.status = status
        self.next = None
        self.min = foodlist[0].cost
        self.max = foodlist[0].cost
        for f in foodlist:
            if f.cost > self.max:
                self.max = f.cost
            if f.cost < self.min:
                self.min = f.cost

class StallList:
    def __init__(self, stall):
        self.head = stall
        self.tail = stall

    def push(self, stall):
        self.tail.next = stall
        self.tail = stall
    
    def findbyID(self, ID):
        tmp = self.head
        while tmp is not None:
            if tmp.stallID == ID:
                return tmp
            tmp = tmp.next
        return None
    
    def findbyName(self, string):
        result = []
        tmp = self.head
        while tmp is not None:
            if string in tmp.name:
                result.append(tmp)
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

pizza = Food('Pizza',1,1,'pizzahut/pizza.jpg',200,1)
spaghetti = Food('Mỳ Ý',1,1,'pizzahut/spaghetti.jpg',80,1)
salad = Food('Salad trộn',1,1,'pizzahut/salad.jpg',50,1)
pizzahut = Stall('Pizza Hut',1,'pizzahut/pizzahut.jpg',[pizza,spaghetti,salad],1)

chicken = Food('Gà rán',1,1,'kfc/ga.jpg',100,1)
hamburger = Food('Hamburger',1,1,'kfc/hamburger.jpg',50,1)
rice = Food('Cơm',1,1,'kfc/com.jpg',40,1)
kfc = Stall('KFC',2,'kfc/kfc.jpg',[chicken,hamburger,rice],1)

stalls = StallList(pizzahut)
stalls.push(kfc)
