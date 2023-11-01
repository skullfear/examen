class TransporteUrbano:
    def __init__(self, tipo, marca, modelo):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo

    def obtener_informacion(self):
        return f"Tipo: {self.tipo}, Marca: {self.marca}, Modelo: {self.modelo}"

# Crear instancias de diferentes medios de transporte urbano
autobus = TransporteUrbano("Autobús", "transmilenio", "Volkswagen")
taxi = TransporteUrbano("taxi", "chevrolet", "chevytaxi")
bicicleta = TransporteUrbano("todoterreno", "GW", "700berlin")

# Mostrar la información de los medios de transporte
print("Información del Autobús:", autobus.obtener_informacion())
print("Información del Taxi:", taxi.obtener_informacion())
print("Información de la Bicicleta:", bicicleta.obtener_informacion())
