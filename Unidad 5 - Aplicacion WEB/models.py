from __main__ import app
from flask_sqlalchemy import SQLAlchemy
db= SQLAlchemy(app)
class Preceptor(db.Model):
    __tablename__= 'preceptor'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=False)
    clave = db.Column(db.String(120), nullable=False)    
    cursos = db.relationship('Curso', backref='preceptor')
    
class Curso(db.Model):
    __tablename__= 'curso'
    id = db.Column(db.Integer, primary_key=True)
    anio = db.Column(db.String(80), nullable=False)
    division = db.Column(db.Integer, nullable=False)
    idpreceptor = db.Column(db.Integer, db.ForeignKey('preceptor.id'))        
    estudiante = db.relationship('Estudiante', backref='curso')
    

class Estudiante(db.Model):
    
    __tablename__= 'estudiante'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    dni = db.Column(db.String(10), unique=True, nullable=False)
    idcurso = db.Column(db.Integer, db.ForeignKey('curso.id'))        
    asistencia = db.relationship('Asistencia', backref='estudiante')


class Asistencia(db.Model):
    
    __tablename__= 'asistencia'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.String(10), nullable=False)
    codigoclase = db.Column(db.Integer, nullable=False)
    asistio = db.Column(db.String(2), unique=True, nullable=False)
    justificacion = db.Column(db.String(40), unique=True, nullable=False)
    idestudiante = db.Column(db.Integer, db.ForeignKey('estudiante.id'))        
    
    
    