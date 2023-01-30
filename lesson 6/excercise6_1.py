class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas


class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


c = Coche("rojo", 4, 5, 200, 1400)

print("Color:", c.color)
print("Ruedas:", c.ruedas)
print("Puertas:", c.puertas)
print("Velocidad:", c.velocidad)
print("Cilindrada:", c.cilindrada)
