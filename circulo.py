from figura import *

class Circulo(Dibujable):
    def dibujar_en_plano(self, punto1, punto2):
        # Implementación para dibujar un círculo en el plano usando los dos puntos como base
        print(f"Dibujando un círculo con coordenadas {punto1} y {punto2}")