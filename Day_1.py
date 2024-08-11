print(2 + 1) # addition(+)
print(3 - 3) # subtraction(-)
print(2 * 2) # multiplication(*)
print(2 / 2) # division(/)
print(3 ** 2) #exponential(**)
print(3 % 2) #modulus(%) devuelve el residuo factorial
print(3 // 2) #floor division operator(//) division entera, ignorando cualquiera parte del resultado decimal

#checking data types, verificando tipos ede datos
#en python no es necesario declarar el tipo de dato

print(type(10)) #int
#la funcion type es un forma para determinar un objeto
numero = 10
tipo_numero = type(numero)
nombre_tipo = tipo_numero.__name__
print(nombre_tipo)  # Imprime: int

print(type(3.14)) #float
print(type(1 + 3j)) #complex
print(type('Asabeneh')) #string
print(type([1, 2, 3])) #list es tipo de dato mutable y ordenado, se declara con corchetes o con list( 1, "3")
#Puede contener cualquier tipo de dato. 
print(type({'name': 'Asabeneh'})) #Dilctionary
print(type({9.8 , 3.3, 2.3})) #set son valores que no pueden duplicar, esto se podria utilizar para
#eleminar duplicados de una coleccion de elementos, verificacion de pertenecia, operacion de conjuntos
#los datos no estan ordenados
print(type((9.3, 3.2, 3.1))) #tuple los datos estan ordenados y son inmutables

dato = (3, 2, 10)
print(dato[0])#accendiendo a la posicion 0 de la tuple