from Vehiculo import Vehiculo
class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindraje):
        super().__init__(marca, modelo)
        self._cilindraje = cilindraje

    @property
    def cilindraje(self):
        return self._cilindraje
    
    @cilindraje.setter
    def cilindraje(self, nuevo_cilindraje):
        if nuevo_cilindraje <10:
            raise ValueError("Cilindraje Erróneo.")
        self._cilindraje = nuevo_cilindraje

    def __str__(self):
        return f"{super().__str__()}, Cilindraje: {self._cilindraje}"