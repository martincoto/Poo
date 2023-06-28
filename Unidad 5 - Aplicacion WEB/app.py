
import hashlib
import hmac
from flask import Flask, request, render_template,url_for,session,redirect
from functools import wraps

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
    
    if request.method=='POST':
        rol=request.form.get('rol')
        if rol=='preceptor':
            preceptor_actual= Preceptor.query.filter_by(correo=request.form['correo']).first()
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
        elif rol=='padre':
            session['rol']='padre'
            session['logged_in']= True
            return redirect(url_for('opciones'))
    else:
	    return render_template('index.html')
 
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            return render_template('index.html',error="Tiene que ingresar a su cuenta antes")
        return f(*args, **kwargs)
    return decorated_function
 
@app.route('/opciones')
@login_required
def opciones():
    return render_template('opciones.html',rol=session.get('rol'))

@app.route('/opciones/registrar_asistencia',methods=['POST','GET'])
@login_required
def regasistencia():
    id_preceptor=session.get('idpreceptor')
    
    if id_preceptor:
        preceptor=Preceptor.query.get(id_preceptor)
        if preceptor:
            if request.method == 'POST':
                if not request.form['curso']:
                    return render_template('asistencia.html',rol=session.get('rol'),cursos=preceptor.curso,curso_seleccionado=None)
                else:
                    curso_seleccionado=request.form['curso']
                    clase=request.form['clase']
                    fecha=request.form['fecha']
                    return redirect(url_for('guardar_asistencia',fecha=fecha,curso_seleccionado=curso_seleccionado,clase=clase))
            else:
                return render_template('asistencia.html',rol=session.get('rol'),cursos=preceptor.cursos,curso_seleccionado=None,)

@app.route('/registrar_asistencia/<fecha>/<curso_seleccionado>/<clase>',methods=['POST','GET'])
@login_required
def guardar_asistencia(fecha,curso_seleccionado,clase):
    curso=Curso.query.get(curso_seleccionado) 
    estudiantes = sorted(curso.estudiante, key=lambda estudiante: (estudiante.apellido, estudiante.nombre))
    if request.method== 'POST':
        band=True
        asistio=[asistencia.lower() for asistencia in request.form.getlist('asistio[]')]
        for asistencia in asistio:
            if not (asistencia=='s' or asistencia=='n'):
                band=False
        
        
        if band:
            
            justificacion=request.form.getlist('justificacion[]')
            estudiante=request.form.getlist('estudiante_id[]')
            for i in range(len(estudiantes)):
                asis_estudiante = Asistencia()
                asis_estudiante.fecha=fecha
                asis_estudiante.codigoclase=clase
                asis_estudiante.asistio=asistio[i]
                asis_estudiante.justificacion=justificacion[i]
                asis_estudiante.idestudiante=estudiante[i]
                db.session.add(asis_estudiante)
                db.session.commit()
            return render_template('guardar_asistencia.html', aviso="Se ha guardado exitosamente la asistencia",rol=session.get('rol'),estudiantes=estudiantes,fecha=fecha,clase=clase)
        else:
            return render_template('guardar_asistencia.html',rol=session.get('rol'),estudiantes=estudiantes,fecha=fecha,clase=clase,error="Caracter de Asistencia Ingresado Invalido")
    else:
        return render_template('guardar_asistencia.html',rol=session.get('rol'),estudiantes=estudiantes,fecha=fecha,clase=clase)
    
@app.route('/informe',methods=['POST','GET'])
@login_required
def informe():
    id_preceptor=session.get('idpreceptor')
    if id_preceptor:
        preceptor=Preceptor.query.get(id_preceptor)
        if preceptor:
            if request.method == 'POST':
                if not request.form['curso']:
                    return render_template('informe.html',rol=session.get('rol'),cursos=preceptor.cursos)
                else:
                    curso_seleccionado=request.form['curso']
                    print(curso_seleccionado)
                    return redirect(url_for('muestra_informe',curso_seleccionado=curso_seleccionado))
            else:
                return render_template('informe.html',rol=session.get('rol'),cursos=preceptor.cursos)
                
                
@app.route('/informe/<curso_seleccionado>', methods=['GET'])
@login_required
def muestra_informe(curso_seleccionado):
        
    curso=Curso.query.get(curso_seleccionado)
    estudiantes = sorted(curso.estudiante, key=lambda estudiante: (estudiante.apellido, estudiante.nombre))
    asist=[]
    for cant in range(len(estudiantes)):
        asist.append([0,0,0,0,0,0,0])
    asistencias = Asistencia.query.all()
    i=0
    for estudiante in estudiantes:
        for asistencia in asistencias:
            if asistencia.idestudiante==estudiante.id:
                if asistencia.asistio=='s':
                    if asistencia.codigoclase==1:
                        asist[i][0]+=1
                    else:
                        asist[i][3]+=1
                else:
                    if asistencia.codigoclase==1:
                        if asistencia.justificacion=='':
                            asist[i][2]+=1
                            asist[i][6]+=1
                        else:
                            asist[i][1]+=1
                            asist[i][6]+=1
                    else:
                        if asistencia.justificacion=='':
                            asist[i][5]+=1
                            asist[i][6]+=0.5
                        else:
                            asist[i][4]+=1
                            asist[i][6]+=0.5
        i+=1
        
    return render_template('informe_muestra.html',rol=session.get('rol'),estudiantes=estudiantes,asistencias=asist)         
    


if __name__ == '__main__':
    with app.app_context():
        db.create_all() 
        
    app.run()	