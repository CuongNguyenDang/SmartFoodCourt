"""
The flask application package.

---> Don't care this file

"""

import os
import views
from flask import Flask, render_template
app = Flask(__name__, template_folder="static")
