from werkzeug.security import check_password_hash

class Usuario():

    def __init__(self, id_usuario, cod_rol, Tipo_documento, Numero_documento, Nombre, Correo, Telefono, Contraseña) -> None:

        self.id_usuario = id_usuario
        self.user = Correo
        self.password = Contraseña

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)
        