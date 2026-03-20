from abc import ABC, abstractmethod

class Figura(ABC):
    
    def __init__(self, color):
        self._color = color
        
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, nuevo_color):
        self._color = nuevo_color
        
    def __str__(self):
        return f"Color: {self._color}"
    
    @abstractmethod
    def area(self):
        pass
