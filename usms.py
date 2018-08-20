from flask import Flask, render_temlate
app = Flask(__name__)

@app.route("/")
def home():
    return render_temlate('index.html')

@app.route("/")
def login():
    return render_temlate('login.html')

@app.route("/")
def register():
    return render_temlate('register.html')

@app.route("/")
def contact():
    return render_temlate('contact.html')

@app.route("/")
def notFound():
    return render_temlate('404.html')
    

if __name__ == '__main__':
    app.run(debug=True)