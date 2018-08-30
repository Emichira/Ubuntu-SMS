from flask import render_template, url_for, flash, redirect, request
from usms import app, db, bcrypt
from usms.forms import RegistrationForm, LoginForm
from usms.models import User
from flask_login import login_user

@app.route("/", methods=['GET'])
@app.route("/home", methods=['GET'])
def home():
    return render_template('index.html', title='USMS')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, phone=form.phone.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created. You are able to Log In', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard/index.html', title='Home')

@app.route("/administration")
def administration():
    return render_template('dashboard/pages/administration.html', title='Administration')

@app.route("/api_documents")
def api_documents():
    return render_template('dashboard/pages/api-documents.html', title='API Documents')

@app.route("/pages_404")
def pages_404():
    return render_template('dashboard/pages/pages-error-404.html', title='Error404')

@app.route("/pages_500")
def pages_500():
    return render_template('dashboard/pages/pages-error-500.html', title='Service Error')

@app.route("/profile")
def profile():
    return render_template('dashboard/pages/pages-profile.html', title='User Account')    

@app.route("/smpp")
def smpp():
    return render_template('dashboard/pages/smpp.html', title='smpp')
