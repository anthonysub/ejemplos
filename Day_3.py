#operadores - operators

#Boleano tipo de dato que costa de 2 valores True y False
print(True) 
print(False)

#tipos de operadores de asignación
valor_1 = 1
valor_1 += 1 # es igual a  valor_1 = valor_1 + 1 
valor_1 -= 1 #resta
valor_1 *= 1 #multiplicacion
valor_1 /= 1 #division
valor_1 /= 1 #division entera
valor_1 %= 1 #Residuo
valor_1 **= 1 #Exponente
valor_1 &= 1 #operador and
valor_1 |= 1 #operador or
valor_1 ^= 1 #operador xor
valor_1 >>= 1 #operador de dezplazamiento, 1 posiscion asignada al resultado
valor_1 <<= 1 #operador de deplzamiento ala izqauierda.

#ejemplos de floats, example: Floats
print('Floating Point Number, PI', 3.1416)
print('Floating Point Number, gravity', 9.81)

#ejemplos de numberos complejos, Example> complex numbers
print('Complex number', 1 + 1j)
print('Multiplying complex numbers:, ', (1 + 1j) * (1-1j))

#ejemplos / examples

a = 3 # a es una variable y 3 es el valor integrado
b = 2 # b es una variable y 2 es un valor integrado 

# arithmetic operating and assigning the result to a variable / operaciones aritmeticas y asignacion de resultados

total = a + b 
diff = a - b 
product = a * b
division = a / b 
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is built-in function try to avoid overriding builtin functions
#deberia haber usado suma en lugar de total, pero suma es una funcion incorporada. intente evitar anular funciones incorporadas

print(total) #imprimir en consola 
print('a + b =', total)
print('a - b =', diff)
print('a * b =', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

#declaring values and organizing them together / declarando valoresw y organizandolos
num_one = 3
num_two = 2

#arithmetic operations

total =  num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

#printing values with label / imprimiendo valores con etiqueta

print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)

#calculating area of a circle / calculando el area de un circulo
radius  = 10
area_of_circle = 3.14 * radius ** 2
print('Area of a circle: ', area_of_circle)

#calculating a weight of an object / calculando el peso de un objeto
mass = 75
gravity = 9.81
weigth = mass * gravity
print( weigth, "N")

print(3 > 2) #True, because 3 is greater than 2 / Verdadero, porque 3 es mayor que 2
print(3 >= 2) #True, because 4 is greater than 2 / Verdadero, porque 3 es mayor que 2
print(3 < 2) #Faslse, beacause 3 is greater than 2 / Falso porque 3 es mayor que 2                                                                                                                                                                                                                                                 
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# Comparing something gives either a True or False - Comparar algo da como resultado Verdadero o Falso
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)

# is 
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print (x is y) #True, porque 'y' es una referencia al mimos objeto que 'x'
print (x is z) #False, porque 'z' es un objeto diferente con el mimso contenido

#is not
print(x is not z) #True, oprque 'x' y 'z' son objetos diferentes aunque tengan el mismo contenido

#in
frutas = ['Manzana', 'banana', 'cereza']
print('banana' in frutas) #True, porque 'banana' esta en ; la lista 'frutas
print('uva' in frutas) #False, porque 'uva' no esta en la lista 'frutas'

#not inñ

print('uva' not in frutas) #True, porque 'uva' no esta en la lista 'frutas'
print('banana' not in frutas) #False, porque 'banana' si esta en la lista 'frutas'

#logical operators - operadores logicos
#Unlike other programing languages python uses keywords and, or and not for logical operators. / a diferencia de otros lenguajes de programacion pytho usa palabras clave
#Logicla operators are used to combine conditional statements

#and
print(3 > 2 and 4 > 3)  # True - porque ambas declaraciones son verdaderas
print(3 > 2 and 4 < 3)  # False - porque la segunda declaración es falsa
print(3 < 2 and 4 < 3)  # False - porque ambas declaraciones son falsas
print('True and True:', True and True)  # True

edad = 25
have_license = True

if edad >= 18 and have_license: #colocar : despues de una condicional
    print("puede conducir")

#or
print(3 > 2 or 4 > 3) #True, porque ambas declaraciones son verdaderas
print(3 > 2 or 4 < 3) #True, porque una declaracion es verdadera
print(3 < 2 or 4 < 3) #False, porque ambas declaraciones son falsas
print(' True or False', True or False) #True

dia = "Sabado"
es_vacaciones = False

if dia == "Sabado" or dia == "Domingo" or es_vacaciones:
    print("No hay que ir a trabajar") #Al menos una condicion es verdadera

#not
print(not 3 > 2) #False, porque 3 es verdadero, enotnces no True da False

a = True
print(not a)  # False, porque a es True y not True es False

b = False
print(not b)  # True, porque b es False y not False es True

x = 5
y = 10

if not x > y:
    print("x no es mayor que y")  # True, porque x > y es False y not False es True

