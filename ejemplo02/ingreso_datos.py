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

        club = Club(
            nombre=nombre,
            deporte=deporte,
            fundacion=int(fundacion)
        )

        session.add(club)

session.commit()
with open("data/datos_jugadores.txt", "r", encoding="utf-8") as file:
    for line in file:

        club_nombre, posicion, dorsal, nombre = line.strip().split(";")

        # search club in database
        club_busqueda = session.query(Club)\
                               .filter_by(nombre=club_nombre)\
                               .one()

        jugador = Jugador(
            nombre=nombre,
            dorsal=int(dorsal),
            posicion=posicion,
            club=club_busqueda
        )

        session.add(jugador)

session.commit()