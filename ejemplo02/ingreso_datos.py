with open("data/datos_clubs.txt", "r", encoding="utf-8") as file:
    for line in file:
        nombre, deporte, fundacion = line.strip().split(";")

        print("Name:", nombre)

        
with open("data/datos_jugadores.txt", "r", encoding="utf-8") as file:
    for line in file:
        club, posicion, dorsal, nombre  = line.strip().split(";")

        print("Name:", nombre)
