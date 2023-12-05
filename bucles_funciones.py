def numeritos (list_numerito):
  for numerito in list_numerito:
    if numerito % 2 == 0: 
      print (f"el numero {numerito} es par")
    else: 
      print ( f"el numero {numerito} es impar")
  return numerito

numeritos([1,2,3,4])
print (numeritos([1,2,3,4]))

def contar (digitos_numero):
  return len(str(digitos_numero))

print ("el numero de digitos es:",contar(148))

def numero_maximo (list_numeros):
  maximo = list_numeros [0]
  for number in list_numeros:
    if number > maximo:
      maximo=number
  return maximo

numero_maximo([3,4,10,2])
print (numero_maximo([3,4,10,2]))

def area (altura,base):
  return ((altura*base)/2)
altura=5
base=2

print (area(altura,base))

def verificar_signo (los_palos):
  for palo in los_palos: 
    if palo >0:
      print(f"el palo {palo} es positivo")
    elif palo <0: 
      print (f"el palo {palo} es negativo")
    else:
      print (f"el palo {palo} es 0")
  return palo

print (verificar_signo([1,-5,4,0]))

def contador_letras(letras):
  for letra in letras:
    return len (letra)

contador_letras(["hola"])
print (contador_letras(["hola"]))
