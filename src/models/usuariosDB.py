from utiles.db import db


class dbUsuarios(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100))
    contrasena = db.Column(db.String(100))

    def __init__(self, fullname, cotrasena):
        self.fullname = fullname
        self.contrasena = cotrasena
