nombre = input("Cual es su nombre? ")
ventas = input("Cuantas son sus ventas? ")

ventas = int(ventas)

comision = ventas * 13 / 100

print(f"OK {nombre} tu comision por ventas este mes son {comision}")
