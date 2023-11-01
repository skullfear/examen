from abc import ABC, abstractmethod


class Dibujable(ABC):
    @abstractmethod
    def dibujar_en_plano(self):
        pass
