from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "clave_super_secreta"  # Necesario para usar flash
#Login
@app.route('/')
def login():
    return render_template('auth/login.html')


#Olvidé COntraseña
@app.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        email = request.form.get("email")

        # 🔹 Ejemplo de validación sin BD
        if email != "usuario@ejemplo.com":
            flash("El correo no está registrado")
            return redirect(url_for("forgot_password"))

        flash("Se ha enviado un enlace de recuperación a tu correo")
        return redirect(url_for("forgot_password"))

    return render_template("auth/forgot_password.html")


#Cambio Obligatorio Contraseña
@app.route('/cambio_obligatorio')
def cambio_obligatorio():
    return render_template('auth/cambio_obligatorio.html')


if __name__ == '__main__':
    app.run(debug=True)