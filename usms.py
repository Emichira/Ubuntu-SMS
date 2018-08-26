from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '18be081e801b18259fc7a92ce165329a'

@app.route("/", methods=['GET'])
@app.route("/home", methods=['GET'])
def home():
    return render_template('index.html', title='USMS')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account Created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'usms@ubuntu.com' and form.password.data == 'iroot':
            flash('You have been logged in!', 'success')
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

if __name__ == '__main__':
    app.run(debug=True)