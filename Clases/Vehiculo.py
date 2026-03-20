class Vehiculo:
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
    
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, nueva_marca):
        self._marca = nueva_marca
        
    @property
    def modelo(self):
        return self._modelo
    @modelo.setter
    def modelo(self, nuevo_modelo):
        self._modelo = nuevo_modelo
    
    def __str__(self):
        return f"Marca: {self._marca}, Modelo: {self._modelo}"