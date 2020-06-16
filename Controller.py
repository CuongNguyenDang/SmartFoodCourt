from abc import abstractmethod 
from flask import render_template

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
        return 0
    
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
        return 0

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