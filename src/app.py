from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

from config import config

#Modelos
from Models.ModelUser import ModelUser

#Entidades
from Models.entities.user import Usuario

app = Flask(__name__)

db = MySQL(app)

app.secret_key = "clave_super_secreta" 

#Login
@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        #print(request.form['Correo'])
        #print(request.form['Contraseña'])
        user= Usuario('', request.form['Correo'], request.form['Contraseña'])
        logged_user=ModelUser.login(db,user)
        if logged_user != None:
            if logged_user.password:
                return redirect (url_for('home'))
            else:
                flash("Contraseña no valida")
                return render_template('auth/login.html')
        else:
            flash("Usuario no encontrado")
        return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')
    
@app.route('/home')
def home():
    return render_template('home.html')
if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()


#Olvidé Contraseña
@app.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        email = request.form.get("email")

        # Validación simulada
        if email == "usuario@ejemplo.com":
            flash("Se ha enviado un enlace de recuperación a tu correo", "success")
        else:
            flash("El correo no está registrado", "error")

        return redirect(url_for("forgot_password"))

    return render_template("auth/forgot_password.html")


#Cambio Obligatorio Contraseña
@app.route('/cambio_obligatorio')
def cambio_obligatorio():
    return render_template('auth/cambio_obligatorio.html')
#Pagina principal
@app.route('/Pagina_principal')
def Pagina_principal():
    return render_template('auth/Principal.html')

if __name__ == '__main__':
    app.run(debug=True)