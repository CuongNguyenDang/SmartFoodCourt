"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template, request,redirect, url_for
from FoodCourt import app
import os
import glob
#import Process
import webbrowser
import Controller
#import order
from Model import stalls
from shutil import copyfile
#import Data report
from Model import stalldata, iData
from  Model import listData
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

@app('/signup')
def signup():
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
 
 
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)




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
@app.route('/order')
def orderMainIU():
    """Renders the order page."""
    i=0
    tmp = stalls.head
    lst=[]
    while i<2:
        lst.append(tmp)
        tmp=tmp.next
        i+=1
    return render_template(
        'order.html',
        stall = lst,
        year=datetime.now().year,
    )
@app.route('/order<name>')
def stallIU(name):
    """Renders the order page."""
    stall = stalls.findbyName(name)[0]
    files = glob.glob('/images/stall/*')
    for f in files:
        os.remove(f)
    copyfile('static/images/%s' %stall.img,'static/images/stall/stall.jpg')
    food = stall.foodlist
    for f in food:
        copyfile('static/images/%s' %f.img,'static/images/stall/food%d.jpg' %food.index(f))
    return render_template(
        'stall.html',
        stall = stall,
        food = food,
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

class OrderView:
    pass #Do nothing