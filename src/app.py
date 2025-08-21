from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "clave_super_secreta" 
#Login
@app.route('/')
def login():
    return render_template('auth/login.html')


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