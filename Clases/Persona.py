class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    
    @nombre.deleter
    def nombre(self):
        del self._nombre
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad < 0:
            raise ValueError("La edad no puede ser negativa.")
        self._edad = nueva_edad

    @edad.deleter
    def edad(self):
        del self._edad

    def saludar(self):
        return f"Hola {self._nombre}, veo que tienes {self._edad} años."
    
    def __str__(self):
        return f"nombre:{self._nombre}, edad:{self._edad}"