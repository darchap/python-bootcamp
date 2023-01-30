entrada = int(input("Introduce un año: "))


def es_bisiesto(entrada):
    if entrada % 4 == 0:
        if entrada % 100 == 0:
            if entrada % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


if es_bisiesto(entrada):
    print("Es bisiesto")
else:
    print("No es bisiesto")
