import math
def area_circulo():
  radio=float(input("El radio del circulo: "))
  if radio<0:
    radio=float(input("Vuelve a introducir el radio del circulo: "))
  area=(radio*radio)*(math.pi)
  print("Area de este circullo es de ", round(area,2))
area_circulo()


def imc():
  peso=float(input("¿Cuanto peso?: "))
  altura=float(input("¿Cuanto mides?: "))
  IMC=peso/(altura*altura)
  if IMC<18.50:
    print("Estas en bajo peso")
  elif 18.50<=IMC<25.00:
    print("Estas en normalidad")
  elif IMC>=25.00:
    print("Estas en sobrepeso")
  else:
    print("Estas en obesidad")
  print(IMC)
imc()


def lee_numero():
  primer_numero=float(input("Introduce un número cualquiera: "  ))
  segundo_numero=float(input("Introduce un número cualquiera: "  ))
  tercer_numero=float(input("Introduce un número cualquiera: "  ))
  return primer_numero,segundo_numero,tercer_numero 
lee_numero()

def mayor(primer_numero,segundo_numero,tercer_numero):
  print(max(mayor))

mayor(primer_numero,segundo_numero,tercer_numero)




import math
def area_circulo():
  radio=float(input("El radio del circulo: "))
  area=(radio*radio)*(math.pi)
  print("Area de este circullo es de ", round(area,2))
area_circulo()