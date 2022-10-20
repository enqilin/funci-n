import math
def area_circulo():
  radio=float(input("El radio del circulo: "))
  if radio<0:
    radio=float(input("Vuelve a introducir el radio del circulo: "))
  area=(radio*radio)*(math.pi)
  print("Area de este circullo es de ", round(area,2))
area_circulo()