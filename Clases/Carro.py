from Clases.Vehiculo import Vehiculo
class Carro(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self._puertas = puertas
    
    @property
    def puertas(self):
        return self._puertas
    @puertas.setter
    def puertas(self, nuevas_puertas):
        if nuevas_puertas < 1:
            raise ValueError("El número de puertas no puede ser menor a 1.")
        self._puertas = nuevas_puertas
    
    def __str__(self):
        return f"{super().__str__()}, Puertas: {self._puertas}"