from flask import render_template, url_for, flash, redirect, request
from usms import app, db, bcrypt
from usms.forms import RegistrationForm, LoginForm
from usms.models import User
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/", methods=['GET'])
@app.route("/home", methods=['GET'])
def home():
    return render_template('index.html', title='USMS')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if (next_page) else redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact')

@app.route("/database")
def database():
    return render_template('dashboard/pages/sample-database.html', title='Database')

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template('dashboard/index.html', title='Dashboard')

@app.route("/administration")
@login_required
def administration():
    return render_template('dashboard/pages/administration.html', title='Administration')

@app.route("/api_documents")
@login_required
def api_documents():
    return render_template('dashboard/pages/api-documents.html', title='API Documents')

@app.route("/profile")
@login_required
def profile():
    return render_template('dashboard/pages/pages-profile.html', title='User Account')    

@app.route("/smpp")
@login_required
def smpp():
    return render_template('dashboard/pages/smpp.html', title='smpp')

@app.route("/pages_404")
def pages_404():
    return render_template('dashboard/pages/pages-error-404.html', title='Error404')

@app.route("/pages_500")
def pages_500():
    return render_template('dashboard/pages/pages-error-500.html', title='Service Error')

