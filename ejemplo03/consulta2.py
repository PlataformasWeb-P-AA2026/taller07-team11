from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from clases import Departamento, Instructor, Curso, Estudiante, Inscripcion, Tarea, Entrega
from config import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Listar cursos cuyo instructor tenga "Zam" en su nombre
cursos = session.query(Curso).join(Instructor).filter(Instructor.nombre.like("%Zam%")).all()

print("Cursos con instructor que contiene 'Zam'")
for c in cursos:
    print("Curso      : %s" % c.titulo)
    print("Instructor : %s" % c.instructor.nombre)
    print("---------")
