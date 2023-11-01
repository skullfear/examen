from circulo import *
from triangulo import *
from rectangulo import *

class Dibujo:
    def __init__(self):
        self.figura = None

    def elegir_figura(self, figura):
        if figura == "circulo":
            self.figura = Circulo()
        elif figura == "triangulo":
            self.figura = Triangulo()
        elif figura == "rectangulo":
            self.figura = Rectangulo()
        else:
            print("Figura no válida.")

    def dibujar_figura(self, punto1, punto2):
        if self.figura:
            self.figura.dibujar_en_plano(punto1, punto2)

# Ejemplo de uso:
dibujo = Dibujo()
figura_elegida = input("Elija la figura a dibujar (circulo, triangulo o rectangulo): ")
dibujo.elegir_figura(figura_elegida)

if dibujo.figura:
    punto1 = input("Ingrese las coordenadas del primer punto (x1, y1): ")
    punto2 = input("Ingrese las coordenadas del segundo punto (x2, y2): ")
    dibujo.dibujar_figura(punto1, punto2)
