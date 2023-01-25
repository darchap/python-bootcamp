weight = float(input("Ingresa tu peso en kg: "))
height = float(input("Ingresa tu estatura en metros: "))

bmi = weight/(height ** 2)

bmir = round(bmi, 2)

print("Tu indice de masa corporal es", bmir)
