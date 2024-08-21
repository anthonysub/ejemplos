# Define el rango para la primera columna
n = 4

# Imprime el encabezado de la tabla
print("a b a^b a^2 a^3")

# Bucle for que recorre los números del 1 al n
for i in range(1, n + 1):
    a = i
    b = 1
    a_b = a ** b
    a_2 = a ** 2
    a_3 = a ** 3
    # Imprime la fila para el valor actual de i
    print(f"{a} {b} {a_b} {a_2} {a_3}")


#definicion de variables

vara = 4
varb = 2
varc = 3
 # if
if vara < varb:
    print("a es menor que b")
#if  and else
if varb > vara:
    print("b es mayor que a")
else:
    print("a es mayor que b")
#while

while vara != varc:
   varc = int(input("Escribe de nuevo c para que sea igual que a: "))
 
#for
for i in range(1, 10, 1):
    print(i)
    if i + 1 == 10:
        print(10)
#función
def funcioncalcular(one, two):
    tree = one * two
    print(f"la multiplicacion de la variable vara({one}) + mas la variable varb({two}) es igual a = {tree}")
funcioncalcular(vara, varb)




text = "This is a test string. This is only a test."
substring = "test"
start = 0
    
while True:
    index = text.find(substring, start)
    if index == -1:
        break
    print(f"{substring} found at index {index}")
    start = index + 1
    