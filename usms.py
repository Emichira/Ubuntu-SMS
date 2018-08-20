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

@app.route("/404")
def notFound():
    return render_template('404.html', title='404')
    

if __name__ == '__main__':
    app.run(debug=True)