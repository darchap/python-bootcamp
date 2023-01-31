f = open("archivo.txt", "w")
f.write("Primer acceso\n")
f.close()

f = open("archivo.txt", "a")
f.write("Segundo acceso")
f.close()
