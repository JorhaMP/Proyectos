import math
from figura import Figura

class Circulo(Figura):
    
    def __init__(self, color, radio):
        super().__init__(color)
        self._radio = radio
        
    @property
    def radio(self):
        return self._radio
    @radio.setter
    def radio(self, nuevo_radio):
        if nuevo_radio < 0:
            raise ValueError("El radio no puede ser negativo.")
        self._radio = nuevo_radio
        
    def area(self):
        return math.pi * (self._radio ** 2)
        
    def __str__(self):
        return f"Circulo - {super().__str__()}, Radio: {self._radio}"