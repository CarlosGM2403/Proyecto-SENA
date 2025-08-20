from werkzeug.security import check_password_hash

class Usuario():

    def __init__(self, id_usuario, cod_rol, Tipo_documento, Numero_documento, Nombre, Correo, Telefono, Contraseña) -> None:

        self.id_usuario = id_usuario
        self.cod_rol = cod_rol
        self.Tipo_documento = Tipo_documento
        self.Numero_documento = Numero_documento
        self.Nombre = Nombre
        self.Correo = Correo
        self.Telefono = Telefono
        self.Contraseña = Contraseña

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)
        