class Alumno:
    def __init__(self, nombre, apellidos, nota):
        self.nombre = nombre
        self.apellidos = apellidos
        self.nota = nota

    def haAprobado(self):
        if self.nota >= 5:
            return print("El alumno ha aprobado")
        else:
            return print("El alumno no ha aprobado")

    def __str__(self):
        return "Nombre: {}, Apellidos: {}, Nota: {}".format(
            self.nombre, self.apellidos, self.nota
        )


a = Alumno("Pepe", "Garcia", 5.3)
b = Alumno("Juan", "Gomez", 4.5)

print(a)
a.haAprobado()
print()
print(b)
b.haAprobado()
