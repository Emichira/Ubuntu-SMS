from usms import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
# User class handles registration and login of users
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.Integer, unique=True)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __init__(self, username, email, phone, password):
        self.username = username
        self.email = email
        self.phone = phone
        self.password = password

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.phone}', '{self.image_file}')"
        # return 'User(username=%r, email=%r, phone=%r, image_file=%, password=%r)' % (self.username, self.email, self.phone, self.image_file)

# class Bulk_Sms(db.Model):
# # User class handles Bulk SMS 
#     id = id.Column(db.Integer, primary_key=True)
#     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now)
#     cotent = db.Column(db.text, nullable=False)
#     sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     recipient = db.Column(db.Integer, nullable=False)
#     status = db.Column(db.Boolean, default=False, nullable=False)

#     def __repr__(self):
        # return f"Bulk_Sms('{self.date_posted}', '{self.cotent}', '{self.sender_id}', '{self.recipient}', '{self.status}')"


