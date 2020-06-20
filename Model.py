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
        
#Nam's Class_____________________
class iData:
    def __init__(self,payment,cash,mobilemoney,numofCus,pager,bestseller):
        self.payment = payment
        self.cash = cash
        self.mobilemoney = mobilemoney
        self.numofCus = numofCus
        self.pager = pager
        self.bestseller = bestseller
class Stallinfo:
    def __init__(self,idstall,day,month,date,idvo,iData):
        self.idstall = idstall
        self.day = day
        self.month = month
        self.date = date
        self.idvo = idvo
        self.iData = iData
        self.next = None
class StallinfoList:
    def __init__(self, stall):
        self.head = stall
        self.tail = stall

    def push(self, stall):
        self.tail.next = stall
        self.tail = stall
    
    def findbyidstall(self, idstall):
        tmp = self.head
        while tmp is not None:
            if tmp.idstall == idstall:
                return tmp
            tmp = tmp.next
        return None
    def findbyday(self, day):
        tmp = self.head
        while tmp is not None:
            if tmp.day == day:
                return tmp
            tmp = tmp.next
        return None
    def findbymonth(self, month):
        tmp = self.head
        while tmp is not None:
            if tmp.month == month:
                return tmp
            tmp = tmp.next
        return None
    
    def clear(self):
        self.__init__(None)


data0302 = iData(350,200,150,26,5,"Hamburger")
data2408 = iData(400,200,200,30,7,"Chips")
data1903 = iData(1000,150,850,75,15,"Pho Bo")
stalldata1 = Stallinfo(1302,20,5,"20:5:2020","Nam-123", data0302)
stalldata2 = Stallinfo(2408,1,6,"1:6:2020","T-456", data2408)
stalldata3 = Stallinfo(1903,30,4,"30:4:2020","DCDTA-5", data1903)
stalldata = StallinfoList(stalldata1)
stalldata.push(stalldata2)
stalldata.push(stalldata3)
#__________________end Nam's Class