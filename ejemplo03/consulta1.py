from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from clases import Departamento, Instructor, Curso, Estudiante, Inscripcion, Tarea, Entrega
from config import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Listar entregas: nombre del estudiante, titulo de la tarea, nombre del instructor
entregas = session.query(Entrega).all()

print("Presentación de Entregas")
for e in entregas:
    print("Estudiante : %s" % e.estudiante.nombre)
    print("Tarea      : %s" % e.tarea.titulo)
    print("Profesor   : %s" % e.tarea.curso.instructor.nombre)
    print("---------")
