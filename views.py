"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, redirect, url_for
from FoodCourt import app
import os
import webbrowser
import Controller
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
    select = str(request.form.get('comp_select'))
    
    # return render_template(
    #     "pay.html"
    # )
    if select == "thirdService":
        url = getUrl(100000)
        return redirect(url)

    
    return(str(select)) # just to see what select is



# @app.route('/select', methods = ['POST'])
# def pay():
#     webbrowser.open_new('http://127.0.0.1:5000/table')
#     v = PayView()
#     controller = Controller.Payment(None,None,None,v)
#     controller.startPay()
#     return render_template('index.html')

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
