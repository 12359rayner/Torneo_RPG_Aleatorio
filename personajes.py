import random

class Personaje:
    def __init__(self, nombre, vida_maxima, ataque, defensa):
        self.nombre = nombre
        self.vida_maxima = vida_maxima
        self.vida_actual = vida_maxima
        self.ataque = ataque
        self.defensa = defensa

    def recibir_danio(self, cantidad):
        self.vida_actual -= cantidad
        if self.vida_actual < 0:
            self.vida_actual = 0

    def esta_vivo(self):
        return self.vida_actual > 0

    def reiniciar_vida(self):
        self.vida_actual = self.vida_maxima

class Campesino(Personaje):
    def __init__(self, nombre="Campesino Comun"):
        super().__init__(nombre, vida_maxima=40, ataque=8, defensa=4)

class Guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida_maxima=60, ataque=12, defensa=8)

class Asesino(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida_maxima=55, ataque=25, defensa=5)

class Paladin(Personaje):
    def __init__(self, nombre):
        # Tanque: Mucha defensa, ataque moderado
        super().__init__(nombre, vida_maxima=65, ataque=10, defensa=12)

class Salvaje(Personaje):
    def __init__(self, nombre):
        # Mucha vida, ataque decente, baja defensa
        super().__init__(nombre, vida_maxima=85, ataque=13, defensa=4)
