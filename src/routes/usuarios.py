from flask import Blueprint, render_template, request, redirect,flash
from models.usuariosDB import dbUsuarios
from utiles.db import db

usuarioss = Blueprint('dbUsuarios', __name__)


@usuarioss.route('/')
def index():
    usu_list = db.session.query(dbUsuarios).all()

    print(usu_list)

    return render_template('login.html', usu_list=usu_list)


@usuarioss.route('/añad', methods=['POST'])
def add_usu():

    fullname = request.form['fullname']
    contrasena = request.form['contrasena']

    new_usuario = dbUsuarios(fullname, contrasena)

    db.session.add(new_usuario)
    db.session.commit()
    flash('contacto añadido')
    return redirect('/')


@usuarioss.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    usu = dbUsuarios.query.get(id) 
    if request.method == "POST":
       
        usu.fullname = request.form['fullname']
        usu.contrasena = request.form['contrasena']
        db.session.commit()
        flash('contacto actualizado')
        return redirect('/')
    
      
    return render_template('actualizar.html', usu=usu)


@usuarioss.route('/delete/<id>')
def delete(id):
    usu = dbUsuarios.query.get(id)
    db.session.delete(usu)
    db.session.commit()
    flash('eliminado')
    return redirect('/')
