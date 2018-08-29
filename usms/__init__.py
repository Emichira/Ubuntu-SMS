from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# app initiliazation
app = Flask(__name__)
app.config['SECRET_KEY'] = '18be081e801b18259fc7a92ce165329a'

# initialize our db
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Mich$anuel1@localhost/ubuntu_usms'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
app.debug = True
db = SQLAlchemy(app)

from usms import routes