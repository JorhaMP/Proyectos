from Animal import Animal
class Gato(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self._raza = raza
    @property
    def raza(self):
        return self._raza
    @raza.setter
    def raza(self, nueva_raza):
        self._raza = nueva_raza
    
    def __str__(self):
        return f"Gato: {self._nombre}, Edad: {self._edad} años, Raza: {self._raza}"
    
    def descripcion(self):
        return f"🙀{self._nombre} es un gato de {self._edad} años y de raza {self._raza}."