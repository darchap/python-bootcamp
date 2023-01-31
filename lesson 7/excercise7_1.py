import operaciones as ops


def main():
    operador1 = 5
    operador2 = 7

    suma = ops.suma(operador1, operador2)
    resta = ops.resta(operador1, operador2)
    multiplicacion = ops.multiplicacion(operador1, operador2)
    division = round(ops.division(operador1, operador2), 2)

    print(f"El operador 1 es: {operador1}")
    print(f"El operador 2 es: {operador2}")
    print()
    print(f"La suma es: {suma}")
    print(f"La resta es: {resta}")
    print(f"La multiplicacion es: {multiplicacion}")
    print(f"La division es: {division}")


if __name__ == "__main__":
    main()
