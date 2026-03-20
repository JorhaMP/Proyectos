class Animal:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad < 0:
            raise ValueError("La edad no puede ser negativa.")
        self._edad = nueva_edad
    
    def __str__(self):
        return f"Animal: {self._nombre}, Edad: {self._edad} años"
    
    def descripcion(self):
        return f"{self._nombre} es un animal de {self._edad} años."