"""
The flask application package.
"""

from flask import Flask, render_template
app = Flask(__name__, template_folder= "static")

import views
import os

PEOPLE_FOLDER = os.path.join('static', 'images')

app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

