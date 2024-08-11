#strings
#Creating a String - Creando una cadena. 
letter = 'p'
print(letter)
print(len(letter))
greeting = 'hello, wordl!'
print(greeting)
print(len(greeting))
setence = "I hope you are enyoging 30 days of Python Challenge"
print(setence)
print(len(setence))

#multiline string is created by using triple single (''') or triple double quotes
#("""). See the example below.

multiline = """I am teacher and enjoy teaching
I didn't find anything as rewarding as empowering peaple.
That is why I created 30 days of python"""
print(multiline)
print(len(multiline))

#string concatenation
first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '

full_name = first_name + space + last_name
print(full_name)

print(len(first_name)) #8
print(len(last_name)) #7
print(len(first_name) > len(last_name)) #True
print(len(full_name)) #16

#Escape Sequences in Strings / secuencias de escape en cadenas
# \n  new line
# \t Tab means(8 spaces)
# \\ Back slash
# \' Single quote
# \" Double quote

print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces 
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') # To write a backslash, poara colocar una barra se colooca otra 
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote
#para colocar comillas doble se utiliza barra invertida

#string formatting - formato de cadena
# %s / string

nombre = "anthony"
edad = 23
mensaje = "Hola, mi nombre es %s y tengo %s." % (nombre, edad)
print(mensaje)

# %d integers (enteros)
edad2 = 25
mensaje2 = "Tengo %d de vida" % edad2
print(mensaje2)

# %f floating point numbers  / num3eros de punto flotante
precio = 49.99
mensaje3 = "El precio es de %f" % precio
print(mensaje3)

# %.number of digitsf / floating point numbers with fixed precision  - numeros de punto folotante con precision fija
precio2  = 49.99
mensaje4 = " el precio  es de %.2f quetzales" % precio2
print(mensaje4) 

#New stylek string formatting (str.format) - nuevo estilo de formato de cadena

first_name2 = "Asabeneh"
last_name2 = "Yetayeh"
language = "Python"
formated_string = "I am {}  {}. I teach {} ".format(first_name2, last_name2, language)
print(formated_string)

a = 4
b = 3

print("{} + {} = {}".format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

#strings and numbers

radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string2  = "El are of a circle with a radius {} is {:.2f}.".format(radius, pi, area)
print(formated_string2)

# string interpolation / f-string 
c = 1
d = 3

print(f"{a} + {b} = {a + b}")
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

#python strings as sequeneces of characters /  cadenas de python como secuencias de caracteres
#unpacking characters / desempacando personajes

language2 = "Python"
a, b, c, d, e, f = language2
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#accesing characters in strings by index / acceso a caracteres en cadenes por indice

language3 = "python"
first_letter = language3[0]
print(first_letter)

last_index = len(language3) - 1 #se obtiene la longitud y se elimina uno para obtener el indice 
last_letter = language3[last_index]
print(last_letter) # n

# si se decia comenzar a la inversa se utiliza el indice negativo
#if we want to start fromo right end we can use negative indexing, -1 is the last index

language4 = "python"
last_letter2 = language4[-1]
print(last_letter2)

#slicing python string / segmentacion de cadenas de python
#en python se puede dividir cadenas en subcadenas

language5 = "python"
first_three = language5[0:5]
print(first_three)

print(language5[5:])

#reversing a string / saltar caracteres al cortar
greeting1 = "hello, World"
print(greeting[::-1]) # !dlroW ,olleH

#skilpping characters while slicing / saltar caracteres al cortar

idiom = "python"
pto = idiom[0:6:2]
print(pto) # start , stop , step / incremento

#string methods / metodos de cadena
 #capitalize()

challenge = "thrity days of python"
print(challenge.capitalize()) #convierte en mayuscula el primer caracter de la cadena

# count() calcula la cantidad de parametros
 # sintaxis  string.count(substring, start, end)

text = "Python is an amazing programming language. I love Python."
count_python = text.count("Python", 0, 30)
print(count_python)  # Salida: 1

#endswicht() / verifica si una cadina termina con una subcadena especifica.

text = "Hello, world!"
print(text.endswith("world!", 0, 12))  # Salida: False

 #verificacion de multiples sufijos

filename = "document.pdf"
print(filename.endswith((".txt", ".pdf")))  # Salida: True

# expandtabs() / valor predterminado de 8 espacios

text = "Hello\tWorld"
expanded_text = text.expandtabs()
print(expanded_text)
     
     #especificar un numero diferente de espacios 4

expanded_text2 = text.expandtabs(4)
print(expanded_text2) #Hello World

    #usar multiples tabulaciones en la cadena
text3 = "Hello\tWordl\tPython"
expanded_text3 = text3.expandtabs(2)
print(expanded_text3) # #salida> "Hello World Python"



#find() / se utiliza para buscar un subcadena dentro de una  cadena / si la subcadena no se encuentra devuelve -1
 # string.find(substring, start, end)

text4 = "hello world!"
index = text4.find("world")
print(index) # imprimi el comienzo del indice de la subcadena



#rfind()
    #Busqueda simple de la ulitma aparicion
text = "Find the last occurrence of the word 'find' in this sentence. Find It!"
index = text.rfind("find")
print(index)
    #buesqueda con un rango especifico
text = "tghe quick brown fox jumps over the lazy dog."
index = text.rfind("ro", 0 , 25)
