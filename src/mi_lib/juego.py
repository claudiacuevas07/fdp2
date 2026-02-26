# =========================
# JUEGO DEL AHORCADO
# =========================

# ----- INICIALIZACIÓN -----

# Pedir palabra
palabra = ""
while palabra == "":
    palabra = input("Introduce la palabra a adivinar: ").lower().strip()
    if palabra == "":
        print("La palabra no puede estar vacía.")

# Lista con los caracteres
lista_palabra = list(palabra)

# Diccionario con cantidad de cada letra
letras_restantes = {l: lista_palabra.count(l) for l in lista_palabra}

# Variables de control
fallos = 0
letras_acertadas = []
letras_usadas = []

print("\n--- Empieza el juego ---")

# ----- DESARROLLO -----

while fallos < 5 and letras_restantes:

    letra = input("Introduce una letra: ").lower().strip()

    # Validar que sea una sola letra
    if len(letra) != 1 or not letra.isalpha():
        print("Entrada inválida.")
        continue

    # Si ya fue usada
    if letra in letras_usadas:
        print("Ya intentaste esa letra.")
        continue

    letras_usadas.append(letra)

    if letra in letras_restantes:
        print("Acierto")
        letras_acertadas.append(letra)

        # Quitar solo una aparición
        letras_restantes[letra] -= 1
        if letras_restantes[letra] == 0:
            del letras_restantes[letra]
    else:
        print("Fallo")
        fallos += 1

    # Mostrar progreso (comprensión de lista)
    progreso = "".join([l if l in letras_acertadas else "*" for l in palabra])
    print("Palabra:", progreso)
    print("Fallos:", fallos)
    print("-------------------")

# ----- FINAL -----

if not letras_restantes:
    print("Ganaste")
    break
else:
    print("Perdiste")
