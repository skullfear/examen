from figura import *

class Rectangulo(Dibujable):
    def dibujar_en_plano(self, punto1, punto2):
        # Implementación para dibujar un rectángulo en el plano usando los dos puntos como base
        print(f"Dibujando un rectángulo con coordenadas {punto1} y {punto2}")
