import pygame
from abc import ABC, abstractmethod

class Dibujable(ABC):
    @abstractmethod
    def dibujar_en_plano(self, screen, punto1, punto2):
        pass

class Circulo(Dibujable):
    def dibujar_en_plano(self, screen, punto1, punto2):
        # Implementación para dibujar un círculo en la ventana de Pygame
        pygame.draw.circle(screen, (255, 0, 0), punto1, 50)

class Triangulo(Dibujable):
    def dibujar_en_plano(self, screen, punto1, punto2):
        # Implementación para dibujar un triángulo en la ventana de Pygame
        pygame.draw.polygon(screen, (0, 255, 0), [punto1, punto2, (punto1[0] + 100, punto1[1])])

class Rectangulo(Dibujable):
    def dibujar_en_plano(self, screen, punto1, punto2):
        # Implementación para dibujar un rectángulo en la ventana de Pygame
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(punto1[0], punto1[1], punto2[0] - punto1[0], punto2[1] - punto1[1]))

class Dibujo:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
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
            self.figura.dibujar_en_plano(self.screen, punto1, punto2)
            pygame.display.flip()

    def ejecutar(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

if __name__ == "__main__":
    dibujo = Dibujo()
    figura_elegida = input("Elija la figura a dibujar (circulo, triangulo o rectangulo): ")
    dibujo.elegir_figura(figura_elegida)

    if dibujo.figura:
        punto1 = tuple(map(int, input("Ingrese las coordenadas del primer punto (x1, y1): ").split()))
        punto2 = tuple(map(int, input("Ingrese las coordenadas del segundo punto (x2, y2): ").split()))
        dibujo.dibujar_figura(punto1, punto2)
        dibujo.ejecutar()

    pygame.quit()



