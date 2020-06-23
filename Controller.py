from abc import abstractmethod 
from flask import render_template
from momo import getUrl
#main function
#____________________________________________________________________________________

#Pay
#____________________________________________________________
class Payment:
    def __init__(self,thirdService,customerID,payView):
        self.thirdService = thirdService
        self.customerID = customerID
        self.payView = payView
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
        url = getUrl(cost)
        self.payView.showQRCode(url)

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
