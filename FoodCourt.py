"""
The flask application package.

---> Don't care this file

"""

from flask import Flask, render_template
app = Flask(__name__, template_folder= "static")
app.config['MYSQL_HOST'] = 'db4free.net'
app.config['MYSQL_USER'] = 'bk_foodcourt'
app.config['MYSQL_PASSWORD'] = 'Chim1234'
app.config['MYSQL_DB'] = 'bk_foodcourt'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

import views
import os
