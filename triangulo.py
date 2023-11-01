from figura import *

class Triangulo(Dibujable):
    def dibujar_en_plano(self, punto1, punto2):
        # Implementación para dibujar un triángulo en el plano usando los dos puntos como base
        print(f"Dibujando un triángulo con coordenadas {punto1} y {punto2}")
