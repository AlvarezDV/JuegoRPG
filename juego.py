import random

class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque

    def __str__(self):
        return f"Personaje: {self.nombre} - Vida: {self.vida} | Ataque: {self.ataque}"

    def atacar(self, oponente):
        oponente.vida -= self.ataque
        if oponente.vida < 0:
            oponente.vida = 0

    def estaVivo(self):
        return self.vida > 0

# CREACION DE HEROE
nombre = input("Ingresa un nombre para tu Heroe: ")
heroe = Personaje(nombre, 100, 20)

# PLANTILLA DE ENEMIGOS
plantilla = [
    ("Duende", 30, 5),
    ("Esqueleto", 80, 10),
    ("Zombi", 50, 15)
]

# LISTA DE ENEMIGOS PARA LA RONDA
ronda = random.randint(1, 5)
enemigoDerrotado = 0
if ronda > 1:
    print(f"¡Se acercan {ronda} enemigos!")
else:
    print(f"¡Se acerca {ronda} enemigo!")

while heroe.estaVivo() and ronda > 0:
    ronda -= 1

    # SE ESCOGE PLANTILLA PARA CREAR ENEMIGO
    datos = random.choice(plantilla)
    oponente = Personaje(datos[0], datos[1], datos[2])

    print(f"{heroe.nombre} se encuentra con un {oponente.nombre}")

    while heroe.estaVivo() and oponente.estaVivo():
        heroe.atacar(oponente)
        print(f"{heroe.nombre} ataca a {oponente.nombre}")
        print(f"{oponente.nombre} tiene {oponente.vida} de vida restante")

        if oponente.estaVivo():
            oponente.atacar(heroe)
            print(f"{oponente.nombre} ataca a {heroe.nombre}")
            print(f"{heroe.nombre} tiene {heroe.vida} de vida restante")
        
    if heroe.estaVivo():
        print(f"{heroe.nombre} ha ganado la batalla")
        enemigoDerrotado += 1

    if oponente.estaVivo():
        print(f"{heroe.nombre} fue derrotado")

if enemigoDerrotado > 1:
    print(f"{heroe.nombre} derroto a {enemigoDerrotado} enemigos y quedo con {heroe.vida} de vida")
else:
    print(f"{heroe.nombre} derroto a {enemigoDerrotado} enemigo y quedo con {heroe.vida} de vida")

# print(heroe)
# print(Duende)
# print(Esqueleto)
# print(Zombi)