"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request
from FoodCourt import app
import os
import webbrowser
import Controller


#Route
#_____________________________________________________________________________
@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

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



@app.route("/test" , methods=['GET', 'POST'])
def test():
    select = request.form.get('comp_select')
    return(str(select)) # just to see what select is


@app.route('/select', methods = ['POST'])
def pay():
    # webbrowser.open_new('http://127.0.0.1:5000/table')
    v = PayView()
    controller = Controller.Payment(None,None,None,v)
    controller.startPay()
    return render_template('index.html')

#View
#___________________________________________________________________________________

class MainUI:
    pass #Do nothing

class PayView:
    def showPaymentUI(self):
        return render_template('pay.html')
    def showResult(self):
        pass
    def showThirdServiceUI(self):
        pass
    def showQRCode(self,qr):
        return render_template(
            'pay.html',
            qrCode = qr
        )

class OderView:
    pass #Do nothing
