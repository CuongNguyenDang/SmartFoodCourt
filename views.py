"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template, request
from FoodCourt import app
import os
#import Process
import webbrowser
import Controller
from Model import FoodOrder

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
    # return render_template(
    #     'menu.html',
    #     'account.html',
    #     # title='Menu Page',
    #     year=datetime.now().year,
    # )

# @app.route('/about')
# def about():
#     """Renders the about page."""
#     return render_template(
#         'about.html',
#         title='About',
#         year=datetime.now().year,
#         message='Your application description page.'
#     )
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
#Duy's part_________________________________________________________________________
Foodlist =[["Ga",1,"Chua lam"],
      ["Vit",2,"Chua lam"],
      ["Bo",1,"Chua lam"],
      ["Ca",2,"Chua lam"],
      ["Heo",1,"Chua lam"],
      ["Mi",2,"Chua lam"],
      ["Com",2,"Chua lam"],
      ["Hu tieu",1,"Chua lam"],
      ["Bun",1,"Chua lam"],
      ["Coca",1,"Chua lam"],
      ["Pepsi",2,"Chua lam"],
      ["7up",3,"Chua lam"]]
#customer1
or1=[Foodlist[1],Foodlist[3],Foodlist[5],Foodlist[7],Foodlist[9],Foodlist[11]]
ord1=FoodOrder("0001","Phuong Bao Tran") 
for food in or1:
    ord1.addFood(food[0],food[1],food[2])
#customer2
or2=[Foodlist[0],Foodlist[2],Foodlist[4],Foodlist[6],Foodlist[8],Foodlist[10]]
ord2=FoodOrder("0002","Le Quang Duy") 
for food in or2:
    ord2.addFood(food[0],food[1],food[2])
#views
@app.route('/stallorder')
def stallorder():
    
    """Renders the order page."""
    return render_template(
        'stallorder.html',
        # title='Menu Page',
        year=datetime.now().year,
        #customer1
        status=["Chua nhan","Dang lam","Da xong","Da xoa"],
        order1=ord1,
        order2=ord2,
    )

@app.route('/detailorder')
def detailorder():
    """Renders the order page."""
    return render_template(
        'detailorder.html',
        # title='Menu Page',
        year=datetime.now().year,
        order1=ord1,
        order2=ord2,
    )
#Duy's end_________________________________________________________________________
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

# @app.route('/get-text', methods=['POST'])
# def foo():
#     # name = request.form['test']
#     toan = float(request.form['toan'])
#     van = float(request.form['van'])
#     li = float(request.form['li'])
#     hoa = float(request.form['hoa'])
#     sinh = float(request.form['sinh'])
#     su = float(request.form['su'])
#     dia = float(request.form['dia'])
#     gdcd = float(request.form['gdcd'])
#     anh = float(request.form['anh'])

#     #Process.Prediction(toan, van, li, hoa, sinh, su, dia, gdcd, anh)

#     return render_template(
#         'result.html',
#         title='Home Page',
#         year=datetime.now().year,
#         toan = float(request.form['toan']),
#         van = float(request.form['van']),
#         li = float(request.form['li']),
#         hoa = float(request.form['hoa']),
#         sinh = float(request.form['sinh']),
#         su = float(request.form['su']),
#         dia = float(request.form['dia']),
#         gdcd = float(request.form['gdcd']),
#         anh = float(request.form['anh'])
#     )
class OderView:
    pass #Do nothing