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

@app.route("/pages_profile")
def profile():
    return render_template('dashboard/pages/pages-profile.html', title='User Account')    

@app.route("/smpp")
def smpp():
    return render_template('dashboard/pages/smpp.html', title='smpp')

if __name__ == '__main__':
    app.run(debug=True)