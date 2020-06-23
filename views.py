"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template, request, redirect, url_for
from FoodCourt import app
import os
import glob
#import Process
import webbrowser
from Controller import *
#import order
from Model import *
from shutil import copyfile


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

@app.route('/menu')
def menu():
    """Renders the menu page."""
@app.route('/account')
def account():
    """Renders the account page."""
    return render_template(
    #     'menu.html',
         'account.html',
         # title='Menu Page',
         year=datetime.now().year,
     )

# @app.route('/about')
# def about():
#     """Renders the about page."""
#     return render_template(
#         'about.html',
#         title='About',
#         year=datetime.now().year,
#         message='Your application description page.'
#     )

#kduy fixing
@app.route('/order',methods=["GET","POST"])
def orderMainIU():
    """Renders the order page."""
    if request.method == "POST":
        search = request.form['search']
        return redirect('/ordersearch=%s' %search)

    i=0
    tmp = stalllist.head
    lst=[]
    while i<2:
        lst.append(tmp)
        tmp=tmp.next
        i+=1
    return render_template(
        'order.html',
        stall = lst,
    )

@app.route('/ordersearch=<name>',methods=["GET","POST"])
def orderSearchIU(name):
    if request.method == "POST":
        search = request.form['search']
        return redirect('/ordersearch=%s' %search)

    fstall = stalllist.findbyName(name)
    ffood = stalllist.findfood(name)
    return render_template(
        'ordersearch.html',
        stall = fstall,
        food = ffood
    )

@app.route('/order<name>')
def stallIU(name):
    stall = stalllist.findbyName(name)[0]
    food = stall.foodlist
    return render_template(
        'stall.html',
        stall = stall,
        food = food,
    )


@app.route("/pay", methods=['GET', 'POST'])
def pay():
    bill = Bill()
    view = PayView()
    select = request.form.get('comp_select')
    c = PayByMachine(None, None, view)
    if select == 'thirdService':
        c = PayByMachine(None, None, view)
    elif select == 'wallet':
        c = PayByWallet(None, None, view)

    c.startPay()
    c.pay(bill)
    c.saveLog()
    c.finishPay()

    return render_template("index.html")


#Nam's part_______________________________________________________
@app.route('/report', methods=['GET', 'POST'])
def report():
    error = None
    tmp = None
    idata = None
    if request.method == 'POST':
        j = 0
        _tmp = stalldata.head
        while j<3:
            if request.form['idstall'] == str(_tmp.idstall) and request.form['day'] == str(_tmp.day) and request.form['month'] == str(_tmp.month):
                tmp = _tmp
                idata = _tmp.iData
                break
            else:
                _tmp = _tmp.next
                j+=1
                error = ' Có lỗi, xin thử lại !!!'
                
    return render_template('report.html', error=error, stall = tmp , year=datetime.now().year, iData = idata)
@app.route('/mail', methods = ['GET','POST'])
def mail():
    error = None
    if request.method == 'POST':
        if str(request.form['mail']) and str(request.form['mail']).strip():
            error = None
        else: 
            error = 'Xin hãy điền mail !!!'
    return render_template('mail.html', error = error,year=datetime.now().year,)  
@app.route('/update', methods = ['GET','POST'])
def update():
    
    return render_template('update.html',year=datetime.now().year,)   


#Duy's part_________________________________________________________________________
@app.route('/stallorder')
def stallorder():
    """Renders the order page."""
    return render_template(
        'stallorder.html',
        # title='Menu Page',
        year=datetime.now().year,
        state= "Chua nhan"
        
    )
@app.route('/status')
def status():
    """Renders the order page."""
    return render_template(
        'status.html',
        # title='Menu Page',
        year=datetime.now().year,
    )
@app.route('/detailorder')
def detailorder():
    """Renders the order page."""
    return render_template(
        'detailorder.html',
        # title='Menu Page',
        year=datetime.now().year,
    )
#Duy's end_________________________________________________________________________
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

    def showQRCode(self, qrUrl):
        webbrowser.open(qrUrl)



class OrderView:
    pass  # Do nothing
