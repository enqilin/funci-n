def lee_numero():
  return float(input("Introduce un número: "))
def mayor(primer_numero,segundo_numero,tercer_numero):
  if primer_numero> segundo_numero and segundo_numero>tercer_numero:
    return primer_numero
  elif segundo_numero>tercer_numero:
    return segundo_numero
  else:
    return tercer_numero
valores=[]
for i in range(3):
  valores.append(lee_numero())
print("El número mayor es {}".format(mayor(valores[0],valores[1],valores[2])))
    