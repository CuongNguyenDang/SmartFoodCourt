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
        return redirect('/order?=%s' %search)

    search = request.args.get('')
    if search is None:
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
    else:
        fstall = stalllist.findbyName(search)
        ffood = stalllist.findfood(search)
        return render_template(
            'ordersearch.html',
            stall = fstall,
            food = ffood
        )

@app.route('/order<name>', methods=["GET","POST"])
def stallIU(name):
    stall = stalllist.findbyName(name)[0]
    food = stall.foodlist
    if request.method == "POST":
        search = request.form['search']
        food2 = []
        for f in food:
            if search.lower() in f.name.lower():
                food2.append(f)
        return render_template(
            'stall.html',
            stall = stall,
            food = food2,
        )
    return render_template(
        'stall.html',
        stall = stall,
        food = food
    )
#fix cart
@app.route('/add', methods=["GET","POST"])
def addtocart():
    ID = request.args['ID'].split('-')
    food=stalllist.findfoodbyID([int(ID[0]),int(ID[1])])
    cart.addtoCart(food)
    stall = stalllist.findbyID(int(ID[0]))
    return redirect('/order%s' %stall.name)

@app.route('/add2', methods=["GET","POST"])
def addtocart2():
    ID = request.args['ID'].split('-')
    food=stalllist.findfoodbyID([int(ID[0]),int(ID[1])])
    cart.addtoCart(food)
    return redirect('/cart')

@app.route('/less', methods=["GET","POST"])
def less():
    ID = request.args['ID'].split('-')
    food=stalllist.findfoodbyID([int(ID[0]),int(ID[1])])
    cart.less(food)
    return redirect('/cart')

@app.route('/remove', methods=["GET","POST"])
def remove():
    ID = request.args['ID'].split('-')
    food=stalllist.findfoodbyID([int(ID[0]),int(ID[1])])
    cart.remove(food)
    return redirect('/cart')

@app.route("/cart")
def cartIU():
    return render_template(
        'cart.html',
        food = cart.list,
        count = cart.count,
        total = cart.total()
    )

#end fix cart

@app.route("/pay", methods=['GET', 'POST'])
def pay():
    view = PayView()
    # select = request.form.get('comp_select')

    c = PayByMachine(None, None, view)

    c.startPay()
    c.pay(cart.total()*1000)
    c.saveLog()
    c.finishPay()

    return render_template("index.html")

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
    pass #Do nothing

class PayView:
    def showPaymentUI(self):
        return redirect(url_for('home'))
    def showResult(self):
        pass
    def showThirdServiceUI(self):
        pass
    def showQRCode(self,qrUrl):
        return webbrowser.open(qrUrl)

class OrderView:
    pass #Do nothing