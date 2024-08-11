#variables``
"""
firstname
lastname
age
country
city
first_name
last_name
capital_city
_if 
"""
# if we want to use reserved word as a variable
#siqueresmos usar la palabra reserwvada como variable
"""
year_2021
year2021
current_year_2021
birth_year
num1
num2
"""
# nombres invalidos de variables - Invalid Variables
"""
first-name
first@name
first$name
num-1
1num 
"""

#snakecase
# Variables in Python
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }
#funcion para imprimir print y len  paras determinar la longitud en listas, cadenas, tuplas, diccionarios
print('Hello, World!') # The text Hello, World! is an argument- el texto hello, word! es un argumento
print('Hello',',', 'World','!') # it can take multiple arguments, four arguments have been passed
#se puede utilizar multiples argumentos dentro de la funcion
print(len('Hello, World!')) # it takes only one argument

#ejemplos de imprimir valores almacenados en variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

#Declaración de multples variables en una linea - Declaring multiple variable in a line
first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

"""La de claracion de variables con multiple asigancion de valores, es un tecnica que permite
crear y asignar valores a variables simulteneamente. """

#para la obtencion de una entrada del usuario se utiliza la funcipon input()

first_name = input("¿Cual es tu nombre? ")
age = input("¿Cuantos años tienes? ")
print(first_name, "tiene", age, "años")

#Tipo de datos
# Different python data types -  Los diferentes tipos de python
# Let's declare variables with various data types - Declarameos las variables con los diferentes tipos de datos

first_name = 'Asabeneh'     # str - string - cadena
last_name = 'Yetayeh'       # str - string - cadena
country = 'Finland'         # str - string - cadena
city= 'Helsinki'            # str - string - cadena
age = 250                   # int - entero

# Printing out types
print(type('Asabeneh'))     # str - string - cadena
print(type(first_name))     # str - string - cadewna
print(type(10))             # int - entero
print(type(3.14))           # float - flotante - decimales
print(type(1 + 1j))         # complex - complejo - algebra
print(type(True))           # bool - boleano - verdadero o falso - true o false
print(type([1, 2, 3, 4]))     # list  - lista tipo de dato mutable
print(type({'name':'Asabeneh','age':250, 'is_married':250}))    # dict - diccionario - key - value - clave - valor
print(type((1,2)))                                              # tuple - tupla dato no mutable 
print(type(zip([1,2],[3,4])))                                   # set - tipo de dato de conjunto
#se se puede utilizar mediante {"Manzana", " pato"} o con la funcion zip(["perro" , "Gato"]) este tipo de dato no esta ordenado

#Conversion de tipos de datos
# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int1 = 10
print(num_int1)                  # 10
num_str = str(num_int1)
print(num_str)                  # '10'

# str to int or float
num_str1 = '10.6'
num_int2 = int(num_str1.split('.')[0]) # split es un metodo incoropado que se utiliza para dividr las cadenas
#en una lista de subcadenas y basandose de un separador.
print('num_int', num_int2)      # 10
print('num_float', float(num_str1))  # 10.6

num_int3 = int(num_str1.split(".")[1])
print("Obtencion de:", num_int3)

# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']

#funcion split()
# Dividir una cadena por espacios en blanco
cadena = "Esta es una cadena de texto"
subcadenas = cadena.split()
print(subcadenas)  # Salida: ['Esta', 'es', 'una', 'cadena', 'de', 'texto']

# Dividir una cadena por comas
cadena = "Hola,mundo,cómo,estás"
subcadenas = cadena.split(",")
print(subcadenas)  # Salida: ['Hola', 'mundo', 'cómo', 'estás']

# Dividir una cadena por un separador personalizado
cadena = "10-20-30"
subcadenas = cadena.split("-")
print(subcadenas)  # Salida: ['10', '20', '30']

# Limitar el número de divisiones
cadena = "Hola,mundo,mundo,mundo"
subcadenas = cadena.split(",", 2)
print(subcadenas)  # Salida: ['Hola', 'mundo', 'mundo']
