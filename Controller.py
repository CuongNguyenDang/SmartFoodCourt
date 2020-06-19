from abc import abstractmethod 
from flask import render_template
from momo import getUrl
#main function
#____________________________________________________________________________________

#Pay
#____________________________________________________________
class Payment:
    def __init__(self,bill,thirdService,customerID,payView):
        self.bill = bill
        self.thirdService = thirdService
        self.customerID = customerID
        self.payView = payView
    def startPay(self):
        self.payView.showPaymentUI()
    
    #abstract method
    def pay(self,bill):
        pass

    def saveLog(self):
        return 0
    
    def finishPay(self):
        return 0

class PayByMachine(Payment):
    # overriding abstract method
    def pay(self,bill):
        url = getUrl(bill.cost)
        self.payView.showQRCode(url)

class PayByMobile(Payment):
    # overriding abstract method
    def pay(self,bill):
        return 0

class PayByWallet(Payment):
    # overriding abstract method
    def pay(self,bill):
        return 0
#end Pay
#____________________________________________________________
#stall

class food:
    def __init__(self, name, ID, stallID, status):
        self.name = name
        self.foodID = ID
        self.stallID = stallID
        self.status = status

class Stall:
    def __init__(self, name, ID, foodlist, status):
        self.name = name
        self.stallID = ID
        self.foodlist = foodlist
        self.status = status
        self.next = None

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

pizzahut = Stall('Pizza Hut',1,['Pizza','Mỳ Ý','Salad Trộn'], 1)
kfc = Stall('KFC',2,['Gà Rán','Hamburger','Cơm'], 1)
stalls = StallList(pizzahut)
stalls.push(kfc)
