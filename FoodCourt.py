"""
The flask application package.

---> Don't care this file

"""

from flask import Flask, render_template
app = Flask(__name__, template_folder= "static")
app.config['MYSQL_HOST'] = 'sql12.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql12351917'
app.config['MYSQL_PASSWORD'] = 'xNkuISNipg'
app.config['MYSQL_DB'] = 'sql12351917'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

import views
import os