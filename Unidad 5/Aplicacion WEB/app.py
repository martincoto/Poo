from datetime import datetime
import hashlib
import hmac
from flask import Flask, request, render_template,url_for,session,redirect
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config.from_pyfile('config.py')

from models import db 
from models import *


@app.route('/cerrar_sesión')
def cerrar_sesión():
    session.clear()
    return redirect(url_for('index'))
		
@app.route('/', methods=['POST','GET'])
def index():
    print("ayuda 0")
    if request.method=='POST':
        
        rol=request.form.get('rol')
        if rol=='preceptor':
            preceptores=Preceptor.query.all()
            for preceptor in preceptores:
                print(preceptor)
            preceptor_actual= Preceptor.query.filter_by(correo=request.form['correo']).first()
            print(preceptor_actual)
            correo=request.form['correo']
            print(correo)
            if preceptor_actual is None:
                return render_template('index.html', error="El correo no está registrado")
            else:
                clave = request.form['contrasena'].encode('utf-8')
                hashed_password = hashlib.md5(clave).hexdigest()
                verificacion = hmac.compare_digest(hashed_password, preceptor_actual.clave)
                if (verificacion):
                    session['rol']='preceptor'
                    session['idpreceptor']=preceptor_actual.id
                    session['logged_in']= True
                    return redirect(url_for('opciones'))
                else:
                    return render_template('index.html',error="La contraseña es incorrecta")
    else:
	    return render_template('index.html')
 
@app.route('/opciones')

def opciones():
    return render_template('opciones.html',rol=session.get('rol'))

 
    

	
'''@app.route('/nuevo_usuario', methods = ['GET','POST'])
def nuevo_usuario():   
	if request.method == 'POST':
		if not request.form['nombre'] or not request.form['email'] or not request.form['password']:
			return render_template('error.html', error="Los datos ingresados no son correctos...")
		else:
			nuevo_usuario = Usuario(nombre=request.form['nombre'], correo = request.form['email'], clave=generate_password_hash(request.form['password']))       
			db.session.add(nuevo_usuario)
			db.session.commit()
			return render_template('aviso.html', mensaje="El usuario se registró exitosamente")
	return render_template('nuevo_usuario.html')
	
@app.route('/nuevo_comentario', methods = ['GET','POST'])
def nuevo_comentario():
    if request.method == 'POST':
        if  not request.form['email'] or not request.form['password']:
            return render_template('error.html', error="Por favor ingrese los datos requeridos")
        else:
            usuario_actual= Usuario.query.filter_by(correo= request.form['email']).first()
            if usuario_actual is None:
                return render_template('error.html', error="El correo no está registrado")
            else:
                verificacion = check_password_hash(usuario_actual.clave, request.form['password'])
                if (verificacion):                    
                    return render_template('ingresar_comentario.html', usuario = usuario_actual)
                else:
                    return render_template('error.html', error="La contraseña no es válida")
    else:
        return render_template('nuevo_comentario.html')

@app.route('/ingresar_comentario', methods = ['GET', 'POST'])
def ingresar_comentario():
    if request.method == 'POST':
        if not request.form['contenido']:
            return render_template('error.html', error="Contenido no ingresado...")
        else:            
            nuevo_comentario= Comentario(fecha=datetime.now(), contenido=request.form['contenido'], usuario_id =request.form['userId'])    
            db.session.add(nuevo_comentario)
            db.session.commit()
            return render_template('inicio.html') 
    return render_template('inicio.html') 

@app.route('/listar_comentarios')
def listar_comentarios():
   return render_template('listar_comentario.html', comentarios = Comentario.query.all())

@app.route('/listar_comentarios_usuario', methods = ['GET', 'POST'])
def listar_comentarios_usuario():  
    if request.method == 'POST':
        if not request.form['usuarios']:
			#Pasa como parámetro todos los usuarios
            return render_template('listar_comentario_usuario.html', usuarios = Usuario.query.all(), usuario_seleccionado = None )
        else:
            return render_template('listar_comentario_usuario.html', usuarios= None, usuario_selec = Usuario.query.get(request.form['usuarios'])) 
    else:
        return render_template('listar_comentario_usuario.html', usuarios = Usuario.query.all(), usuario_selec = None )   
        
'''
if __name__ == '__main__':
    with app.app_context():
        db.create_all()    
    app.run(debug = True)	