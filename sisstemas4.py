import tkinter as tk

# Variables globales
num1 = ""
num2 = ""
operacion = ""

def calcular():
    global num1, num2, operacion
    try:
        if not num1 or not num2:
            text_var.set("Error: Ingrese ambos números")
            return
        resultado = eval(f"{num1} {operacion} {num2}")
        text_var.set(f"{resultado}")
        num1 = str(resultado)
        num2 = ""
        operacion = ""
    except ZeroDivisionError:
        text_var.set("Error: División por cero")
    except Exception as e:
        text_var.set(f"Error: {str(e)}")

def agregar_digito(digito):
    global num1, num2
    if operacion == "":
        num1 += str(digito)
        text_var.set(num1)
    else:
        num2 += str(digito)
        text_var.set(num2)

def seleccionar_operacion(op):
    global operacion
    operacion = op
    text_var.set(f"{num1} {operacion}")

def limpiar():
    global num1, num2, operacion
    num1 = ""
    num2 = ""
    operacion = ""
    text_var.set("")

# Ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Variable para la caja de texto
text_var = tk.StringVar()

# Crear la caja de texto
entry = tk.Entry(ventana, textvariable=text_var)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botones numéricos
boton1 = tk.Button(ventana, text="1", width=5, command=lambda: agregar_digito(1))
boton1.grid(row=1, column=0)

boton2 = tk.Button(ventana, text="2", width=5, command=lambda: agregar_digito(2))
boton2.grid(row=1, column=1)

boton3 = tk.Button(ventana, text="3", width=5, command=lambda: agregar_digito(3))
boton3.grid(row=1, column=2)

boton4 = tk.Button(ventana, text="4", width=5, command=lambda: agregar_digito(4))
boton4.grid(row=2, column=0)

boton5 = tk.Button(ventana, text="5", width=5, command=lambda: agregar_digito(5))
boton5.grid(row=2, column=1)

boton6 = tk.Button(ventana, text="6", width=5, command=lambda: agregar_digito(6))
boton6.grid(row=2, column=2)

boton7 = tk.Button(ventana, text="7", width=5, command=lambda: agregar_digito(7))
boton7.grid(row=3, column=0)

boton8 = tk.Button(ventana, text="8", width=5, command=lambda: agregar_digito(8))
boton8.grid(row=3, column=1)

boton9 = tk.Button(ventana, text="9", width=5, command=lambda: agregar_digito(9))
boton9.grid(row=3, column=2)

boton0 = tk.Button(ventana, text="0", width=5, command=lambda: agregar_digito(0))
boton0.grid(row=4, column=0)

# Botones de operación
boton_suma = tk.Button(ventana, text="+", width=5, command=lambda: seleccionar_operacion("+"))
boton_suma.grid(row=1, column=3)

boton_resta = tk.Button(ventana, text="-", width=5, command=lambda: seleccionar_operacion("-"))
boton_resta.grid(row=2, column=3)

boton_multiplicacion = tk.Button(ventana, text="*", width=5, command=lambda: seleccionar_operacion("*"))
boton_multiplicacion.grid(row=3, column=3)

boton_division = tk.Button(ventana, text="/", width=5, command=lambda: seleccionar_operacion("/"))
boton_division.grid(row=4, column=3)

# Botón de igual
boton_igual = tk.Button(ventana, text="=", width=5, command=calcular)
boton_igual.grid(row=4, column=2)

# Botón de limpiar
boton_limpiar = tk.Button(ventana, text="C", width=5, command=limpiar)
boton_limpiar.grid(row=4, column=1)

ventana.mainloop()
