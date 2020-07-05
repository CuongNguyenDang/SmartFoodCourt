"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template, request, redirect, url_for, jsonify, make_response
from flask_mysqldb import MySQL
from FoodCourt import app
import MySQLdb
import os
import glob
import json
#import Process
import webbrowser
import Controller
#import order
from Model import *
from shutil import copyfile
from momo import getResult,getUrl
import time
#import Data report

mysql = MySQL(app)

userData = {'id':None,'name':None,'wallet':0,'stall_id':None}
#Route
#_____________________________________________________________________________
@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return render_template(
        'index.html',
    )

#account login
@app.route('/account', methods=['GET', 'POST'])
def account():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM account WHERE username = '"+ username +"'")
        acc = cur.fetchone()
        if acc is None or acc['password'] != request.form['password']:
            error = 'Username hoặc mật khẩu không đúng'
        else:
            userData['id'] = acc['id']
            userData['name'] = acc['name']
            userData['wallet'] = acc['wallet']
            Controller.getCart(cart,acc['cart'])
            cur.execute("SELECT * FROM stall WHERE owner_id = "+ str(userData['id']))
            acc = cur.fetchone()
            if acc is not None:
                userData['stall_id'] = acc['id']
                acc = None
    return render_template('account.html', error=error, user=userData)

@app.route('/recharge', methods=['GET', 'POST'])
def recharge():
    error = None
    if request.method == 'POST':
        money = int(request.form['money'])

        v = PayView()
        url,orderId = getUrl(money)
        v.showQRCode(url)
        waiting_time = 600
        t = 0
        while (getResult(orderId) != 'Success' and t < waiting_time ):
            time.sleep(1)
            t += 1

        if (getResult(orderId) == 'Success'):
            #if paied success
            userData['wallet'] += money
            cur = mysql.connection.cursor()
            cur.execute(f"UPDATE account SET wallet = {userData['wallet']} WHERE id = {userData['id']}")
            mysql.connection.commit()
            return redirect(url_for('account'))
    return render_template('recharge.html', error=error)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        if request.form['password'] != request.form['confirmpass']:
            error = 'Vui lòng xác nhận lại mật khẩu'
        else:
            username = request.form['username']
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM account WHERE username = '"+ username +"'")
            acc = cur.fetchone()
            if acc is not None:
                error = 'Tài khoản đã tồn tại'
            else:
                name = request.form['name']
                password = request.form['password']
                email = request.form['email']
                cur.execute("INSERT INTO account (id, name, username, password, email) VALUES ('AUTO_INCREMENT PRIMARY KEY','"+name+"','"+username+"','"+password+"','"+email+"')")
                mysql.connection.commit()
                return redirect(url_for('account'))
    return render_template('signup.html', error=error)

@app.route('/logout')
def logout():
    text = Controller.convertCarttoText(cart)
    cur = mysql.connection.cursor()
    cur.execute("UPDATE account SET cart='"+text+"' WHERE id = "+str(userData['id']))
    mysql.connection.commit()
    userData['id'] = None
    userData['name'] = None
    cart.cancel()
    return redirect(url_for('account'))

#order 
@app.route('/order',methods=["GET","POST"])
def orderMainIU():
    """Renders the order page."""
    if request.method == "POST":
        search = request.form['search']
        return redirect('/order?search=%s' %search)

    search = request.args.get('search')
    name = request.args.get('stall')
    if search is None and name is None:
        i=0
        tmp = stall_list.head
        lst=[]
        while i<2:
            lst.append(tmp)
            tmp=tmp.next
            i+=1
        return render_template(
            'order.html',
            stall = lst,
        )
    if search is not None:
        fstall = stall_list.findbyName(search)
        tmp = food_list.findbyName(search)
        ffood = []
        for t in tmp:
            ffood.append({'stall':stall_list.findbyID(t.stallID).name,'food':t})
        return render_template(
            'ordersearch.html',
            stall = fstall,
            food = ffood
        )
    else:
        stall = stall_list.findbyName(name)[0]
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
@app.route('/add', methods=["POST"])
def addtocart():
    Controller.addtoCart(cart,int(request.form['ID']))

@app.route('/reduce', methods=["GET","POST"])
def less():
    Controller.reducefromCart(cart,int(request.form['ID']))

@app.route('/remove', methods=["GET","POST"])
def remove():
    Controller.removefromCart(cart,int(request.form['ID']))

@app.route("/cart")
def cartIU():
    return render_template(
        'cart.html',
        food = cart.list,
        count = cart.count,
        total = cart.total
    )

#end cart

@app.route("/pay", methods=['GET', 'POST'])
def pay():
    view = PayView()
    # select = request.form.get('comp_select')
    total = cart.total*1000

    c = Controller.PayByMachine(None, None, view)

    c.startPay()
    c.pay(total)
    c.saveLog()
    c.finishPay()
    # if c.finishPay() == 0:
    #     cart.cancel()
    return render_template(
        'cart.html',
        food = cart.list,
        count = cart.count,
        total = cart.total
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
    def showResult(self,orderId):
        waiting_time = 600
        t = 0
        while (getResult(orderId) != 'Success' and t < waiting_time):
            time.sleep(1)
            t += 1
        if (getResult(orderId) == 'Success'):
            cart.cancel()


class OrderView:
    pass #Do nothing