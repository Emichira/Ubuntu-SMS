from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_heroku import Heroku

# app initiliazation
app = Flask(__name__)
app.config['SECRET_KEY'] = '18be081e801b18259fc7a92ce165329a'

# initialize our db
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Mich$anuel1@localhost/ubuntu_usms'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
app.debug = True
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
heroku = Heroku(app)


from usms import routes