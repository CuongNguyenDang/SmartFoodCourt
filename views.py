"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, redirect, url_for
from FoodCourt import app
import os
import webbrowser
from Controller import *
from Model import Bill
from momo import getUrl

#Route
#_____________________________________________________________________________
@app.route('/', methods = ["GET","POST"])
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/index')
@app.route('/home')
def index():
    return redirect(url_for('home'))

@app.route('/account')
def account():
    """Renders the account page."""
    return render_template(
        'account.html',
        # title='Menu Page',
        year=datetime.now().year,
    )

@app.route('/order')
def order():
    """Renders the order page."""
    return render_template(
        'order.html',
        # title='Menu Page',
        year=datetime.now().year,
    )



@app.route("/pay" , methods=['GET', 'POST'])
def pay():
    bill = Bill()
    view = PayView()
    c = PayByMachine(bill,None,None,view)
    c.startPay()
    c.pay(bill)
    c.saveLog()
    c.finishPay()
    return render_template("index.html")

#View
#___________________________________________________________________________________

class MainUI:
    def __init__(self):
        self.payView = PayView()
        self.orderView = OrderView()

class PayView:
    def showPaymentUI(self):
        return redirect(url_for('home'))
    def showResult(self):
        pass
    def showThirdServiceUI(self):
        pass
    def showQRCode(self,qrUrl):
        webbrowser.open_new_tab(qrUrl)

class OrderView:
    def showOrderUI(self):
        return render_template("index.html")
