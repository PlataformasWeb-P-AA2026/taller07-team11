from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from clases import Departamento, Instructor, Curso, Estudiante, Inscripcion, Tarea, Entrega
from config import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Listar las inscripciones del departamento de Ciencias de la Computación. Por cada inscripción
inscripciones = session.query(Inscripcion).join(Curso, Inscripcion.curso_id == Curso.id).join(Departamento, Curso.departamento_id == Departamento.id).filter(Departamento.nombre == "Ciencias de la Computación").all()

print("Presentación de Entregas")
for i in inscripciones:
    print("Estudiante : %s" % i.estudiante.nombre)
    print("Curso     : %s" % i.curso.titulo)
    print("Profesor   : %s" % i.curso.instructor.nombre)
    print("---------")
