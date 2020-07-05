from abc import abstractmethod 
from flask import render_template
from momo import getUrl
#order
import Model


#main function
#____________________________________________________________________________________

#Pay
#____________________________________________________________
class Payment:
    def __init__(self,thirdService,customerID,payView):
        self.thirdService = thirdService
        self.customerID = customerID
        self.payView = payView
        self.orderId = 0
    def startPay(self):
        self.payView.showPaymentUI()
    
    #abstract method
    def pay(self,cost):
        pass

    def saveLog(self):
        return 0
    
    def finishPay(self):
        return 0

class PayByMachine(Payment):
    # overriding abstract method
    def pay(self,cost):
        if cost <= 1000 : 
            cost = 2000
        url,self.orderId = getUrl(cost)
        self.payView.showQRCode(url)
    
    def finishPay(self):
        self.payView.showResult(self.orderId)

class PayByMobile(Payment):
    # overriding abstract method
    def pay(self,cost):
        return 0

class PayByWallet(Payment):
    # overriding abstract method
    def pay(self,cost):
        return 0
#end Pay
#____________________________________________________________

#order
def addtoCart(cart, ID):
    food = Model.food_list.findbyID(ID)
    cart.addtoCart(food)

def reducefromCart(cart, ID):
    food = Model.food_list.findbyID(ID)
    cart.less(food)

def removefromCart(cart, ID):
    food = Model.food_list.findbyID(ID)
    cart.remove(food)

def getCart(cart, text):
    cart.cancel()
    if text == '':
        return
    foodID = text.split(',')
    for f in foodID:
        ID = f.split('-')
        food = Model.food_list.findbyID(int(ID[0]))
        for i in range(int(ID[1])):
            cart.addtoCart(food)

def convertCarttoText(cart):
    text = ''
    for f in cart.list:
        if text != '':
            text += ','
        text += str(f.foodID)+"-"+str(cart.count[cart.list.index(f)])
    return text