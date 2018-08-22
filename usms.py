from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', title='Home')

@app.route("/login")
def login():
    return render_template('login.html', title='Login')

@app.route("/register")
def register():
    return render_template('register.html', title='Register')

@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard/index.html', title='dashboard')

@app.route("/administration")
def admin():
    return render_template('administration.html', title='404')

@app.route("/api-documents")
def api_documents():
    return render_template('api-documents.html', title='API Documents')

@app.route("/pages-404")
def dashboardNotFound():
    return render_template('pages-error-404.html', title='404')

@app.route("/pages-500")
def serviceError():
    return render_template('pages-error-500.html', title='Service Error')

@app.route("/pages-profile")
def profile():
    return render_template('pages-profile.html', title='User Account')    

@app.route("/smpp")
def smpp():
    return render_template('smpp.html', title='User Account')

if __name__ == '__main__':
    app.run(debug=True)