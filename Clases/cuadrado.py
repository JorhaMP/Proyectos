from figura import Figura
import math

class Cuadrado(Figura):
    
    def __init__(self, color, lado):
        super().__init__(color)
        self._lado = lado
        
    @property
    def lado(self):
        return self._lado
    @lado.setter
    def lado(self, nuevo_lado):
        if nuevo_lado < 0:
            raise ValueError("El lado no puede ser negativo.")
        self._lado = nuevo_lado
        
    def area(self):
        return self._lado ** 2
        
    def __str__(self):
        return f"Cuadrado - {super().__str__()}, Lado: {self._lado}"