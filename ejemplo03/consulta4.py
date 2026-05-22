from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from clases import Departamento, Instructor, Curso, Estudiante, Inscripcion, Tarea, Entrega
from config import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

#Por cada curso, presentar sus tareas asociadas.

cursos = session.query(Curso).join(Tarea).all()

print("Cursos con sus respectivas tareas")
for c in cursos:
    print("Curso      : %s" % c.titulo)
    
for t in c.tareas:
    print("Tarea : %s" % t.titulo)
    print("---------")