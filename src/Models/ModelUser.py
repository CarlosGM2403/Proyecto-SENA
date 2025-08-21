from entities.user import user

class ModelUser():

    @classmethod
    def login (self, db, user):
        try:
            cursor = db.conecction.cursor()
            sql = """Select id_usuario, Correo, Contraseña FROM usuario
                        WHERE Correo = '{}'""".format(user.Correo)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user = user (row[0], row[1], user.check_password(row[2],user.password))
                return user
            else: 
                return None
        except Exception as ex:
            raise Exception(ex)