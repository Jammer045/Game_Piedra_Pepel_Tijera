def obtener_eleccion(jugador):
    eleccion = input(f"{jugador}, elige piedra, papel o tijeras: ").strip().lower()
    if eleccion not in ["piedra", "papel", "tijeras"]:
        print(f"{jugador} ha hecho trampa. Elección inválida.")
        return None
    return eleccion

def determinar_ganador(j1, j2, eleccion1, eleccion2):
    if eleccion1 == eleccion2:
        print("¡Es un empate!")
    elif (eleccion1 == "piedra" and eleccion2 == "tijeras") or \
         (eleccion1 == "papel" and eleccion2 == "piedra") or \
         (eleccion1 == "tijeras" and eleccion2 == "papel"):
        print(f"¡{j1} gana!")
    else:
        print(f"¡{j2} gana!")

def jugar():
    print("Bienvenidos a Piedra, Papel o Tijeras!")
    jugador1 = "Jugador 1"
    jugador2 = "Jugador 2"
    
    eleccion1 = obtener_eleccion(jugador1)
    eleccion2 = obtener_eleccion(jugador2)
    
    if eleccion1 and eleccion2:
        determinar_ganador(jugador1, jugador2, eleccion1, eleccion2)
    else:
        print("Juego terminado debido a una elección inválida.")

if __name__ == "__main__":
    jugar()
