import tkinter as tk

# Variables globales
num1 = ""
num2 = ""
operacion = ""

def calcular():
    global num1, num2, operacion
    try:
        resultado = eval(f"{num1} {operacion} {num2}")
        text_var.set(f"Resultado: {resultado}")  # Actualiza la caja de texto con el resultado
        num1 = str(resultado)
        num2 = ""
        operacion = ""
    except ZeroDivisionError:
        text_var.set("Error: División por cero")
    except:
        text_var.set("Error en la operación")

def agregar_digito(digito):
    global num1, num2
    if operacion == "":
        num1 += str(digito)
        text_var.set(num1)  # Actualiza la caja de texto con el valor de num1
    else:
        num2 += str(digito)
        text_var.set(num2)  # Actualiza la caja de texto con el valor de num2

def seleccionar_operacion(op):
    global operacion
    operacion = op
    text_var.set(f"{num1} {operacion}")  # Muestra la operación seleccionada en la caja de texto

# Ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Variable para la caja de texto
text_var = tk.StringVar()
text_var.set("")

# Crear la caja de texto
entry = tk.Entry(ventana, textvariable=text_var)
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)  # Ajuste en la posición de la caja de texto

# Botones numéricos
boton1 = tk.Button(ventana, text= "1", width=5, command=lambda: agregar_digito(1))
boton1.pack(side=tk.LEFT)

boton2 = tk.Button(ventana, text= "2", width=5, command=lambda: agregar_digito(2))
boton2.pack(side=tk.LEFT)

boton3 = tk.Button(ventana, text= "3", width=5, command=lambda: agregar_digito(3))
boton3.pack(side=tk.LEFT)

boton4 = tk.Button(ventana, text= "4", width=5, command=lambda: agregar_digito(4))
boton4.pack(side=tk.LEFT)

boton5 = tk.Button(ventana, text= "5", width=5, command=lambda: agregar_digito(5))
boton5.pack(side=tk.LEFT)

boton6 = tk.Button(ventana, text= "6", width=5, command=lambda: agregar_digito(6))
boton6.pack(side=tk.LEFT)

boton7 = tk.Button(ventana, text= "7", width=5, command=lambda: agregar_digito(7))
boton7.pack(side=tk.LEFT)

boton8 = tk.Button(ventana, text= "8", width=5, command=lambda: agregar_digito(8))
boton8.pack(side=tk.LEFT)

boton9 = tk.Button(ventana, text= "9", width=5, command=lambda: agregar_digito(9))
boton9.pack(side=tk.LEFT)

boton0 = tk.Button(ventana, text= "0", width=5, command=lambda: agregar_digito(0))
boton0.pack(side=tk.LEFT)

# Botones de operación
boton_suma = tk.Button(ventana, text="+", width=5, command=lambda: seleccionar_operacion("+"))
boton_suma.pack(side=tk.LEFT)

boton_resta = tk.Button(ventana, text="-", width=5, command=lambda: seleccionar_operacion("-"))
boton_resta.pack(side=tk.LEFT)

boton_multiplicacion = tk.Button(ventana, text="*", width=5, command=lambda: seleccionar_operacion("*"))
boton_multiplicacion.pack(side=tk.LEFT)

boton_division = tk.Button(ventana, text="/", width=5, command=lambda: seleccionar_operacion("/"))
boton_division.pack(side=tk.LEFT)

# Botón de igual
boton_igual = tk.Button(ventana, text="=", width=5, command=calcular)
boton_igual.pack(side=tk.LEFT)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="Resultado:")
resultado_label.pack()

ventana.mainloop()
