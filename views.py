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
#import Data report
from Model import stalldata, iData

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

   
@app.route('/account', methods=['GET', 'POST'])
def account():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('account.html', error=error)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # error = None
    # if request.method == 'POST':
    #     if request.form['username'] != 'admin' or request.form['password'] != 'admin':
    #         error = 'Invalid Credentials. Please try again.'
    #     else:
    #         return redirect(url_for('home'))
    return render_template('signup.html')

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
    total = cart.total()*1000

    c = PayByMachine(None, None, view)

    c.startPay()
    c.pay(total)
    c.saveLog()
    if c.finishPay() == 0:
        cart.cancel()
    return render_template(
        'cart.html',
        food = cart.list,
        count = cart.count,
        total = cart.total()
    )

#Duy's part_________________________________________________________________________
#views
@app.route('/stallorder')
def stallorder():
    
    """Renders the order page."""
    return render_template(
        'stallorder.html',
        # title='Menu Page',
        year=datetime.now().year,
        #customer1
        status=["Chưa làm","Đang làm","Đã xong","Đã xóa"],
        order=[ord1,ord2],
        order1=ord1,
        order2=ord2,
    )

@app.route('/testdetail')
def testdetail():
    """Renders the order page."""
    
    return render_template(
        #'detailorder.html',
        'testdetail.html',
        # title='Menu Page',
        year=datetime.now().year,
        order=[ord1,ord2],
        order1=ord1,
        order2=ord2, 
    )
@app.route('/detailorder')
def detailorder():
    """Renders the order page."""
    
    return render_template(
        'detailorder.html',
        #'testdetail.html',
        # title='Menu Page',
        year=datetime.now().year,
        order=[ord1,ord2],
        order1=ord1,
        order2=ord2,    
    )
#Duy's end_________________________________________________________________________
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
#__________________________________________
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