from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def home():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/error")
def notFound():
    return render_template('404.html')
    

if __name__ == '__main__':
    app.run(debug=True)