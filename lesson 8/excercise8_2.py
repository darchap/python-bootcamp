class Vehiculo:
    def __init__(self, marca, modelo, velocidad, puertas):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.puertas = puertas

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Velocidad: {self.velocidad}, Puertas: {self.puertas}"


v = Vehiculo("Ford", "Mustang", 200, 5)

f = open("vehiculo.txt", "w")
f.write(str(v))
f.close()


f = open("vehiculo.txt", "r")
c = f.read()
f.close()
print(c)
