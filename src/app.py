from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('auth/login.html')

@app.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    return render_template("auth/forgot_password.html")

@app.route('/cambio_obligatorio')
def cambio_obligatorio():
    return render_template('auth/cambio_obligatorio.html')

if __name__ == '__main__':
    app.run(debug=True)
