import time

now = time.strftime("%H")
minutes = time.strftime("%M")


def tiempoRestante():
    horasRestantes = 18 - int(now)
    minutosRestantes = 59 - int(minutes)

    print(f"Todavia quedan {horasRestantes} horas y {minutosRestantes} minutos")


if int(now) >= 19:
    print("Ya puedes irte")
else:
    tiempoRestante()
