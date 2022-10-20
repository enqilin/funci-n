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