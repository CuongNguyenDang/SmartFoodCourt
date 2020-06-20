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
