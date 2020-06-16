"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request
from FoodCourt import app
import os
#import Process

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
    return render_template(
        'menu.html',
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
