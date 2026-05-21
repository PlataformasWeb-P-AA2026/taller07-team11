import csv
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from clases import Departamento, Instructor, Curso, Estudiante, Inscripcion, Tarea, Entrega
from config import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

with open("01_departamento.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        session.add(Departamento(id=int(row["id"]), nombre=row["nombre"]))
session.commit()

with open("02_instructor.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        session.add(Instructor(id=int(row["id"]), nombre=row["nombre"]))
session.commit()

with open("03_curso.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        departamento = session.query(Departamento).filter_by(id=int(row["departamento_id"])).first()
        instructor   = session.query(Instructor).filter_by(id=int(row["instructor_id"])).first()
        session.add(Curso(
            id=int(row["id"]),
            titulo=row["titulo"],
            departamento=departamento,
            instructor=instructor
        ))
session.commit()

with open("04_estudiante.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        session.add(Estudiante(id=int(row["id"]), nombre=row["nombre"]))
session.commit()

with open("05_inscripcion.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        estudiante = session.query(Estudiante).filter_by(id=int(row["estudiante_id"])).first()
        curso      = session.query(Curso).filter_by(id=int(row["curso_id"])).first()
        session.add(Inscripcion(
            estudiante=estudiante,
            curso=curso,
            fecha_inscripcion=datetime.strptime(row["fecha_inscripcion"], "%Y-%m-%d %H:%M:%S")
        ))
session.commit()

with open("06_tarea.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        curso = session.query(Curso).filter_by(id=int(row["curso_id"])).first()
        session.add(Tarea(
            id=int(row["id"]),
            titulo=row["titulo"],
            curso=curso,
            fecha_entrega=datetime.strptime(row["fecha_entrega"], "%Y-%m-%d %H:%M:%S")
        ))
session.commit()

with open("07_entrega.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        tarea      = session.query(Tarea).filter_by(id=int(row["tarea_id"])).first()
        estudiante = session.query(Estudiante).filter_by(id=int(row["estudiante_id"])).first()
        session.add(Entrega(
            id=int(row["id"]),
            tarea=tarea,
            estudiante=estudiante,
            fecha_envio=datetime.strptime(row["fecha_envio"], "%Y-%m-%d %H:%M:%S"),
            calificacion=float(row["calificacion"])
        ))
session.commit()

print("Base de datos poblada correctamente.")
