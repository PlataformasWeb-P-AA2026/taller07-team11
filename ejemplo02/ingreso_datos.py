from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ 

from genera_tablas import Club, Jugador


from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

with open("data/datos_clubs.txt", "r", encoding="utf-8") as file:
    for line in file:
        nombre, deporte, fundacion = line.strip().split(";")

        print("Name:", nombre)

        
with open("data/datos_jugadores.txt", "r", encoding="utf-8") as file:
    for line in file:
        club, posicion, dorsal, nombre  = line.strip().split(";")

        print("Name:", nombre)
