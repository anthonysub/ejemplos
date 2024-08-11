import tkinter as tk

def add_number():
    try:
        # Obtener el número actual de la caja de texto
        current_number = int(entry.get())
        # Obtener el número almacenado
        stored_number = int(stored_var.get())
    except ValueError:
        current_number = 0
        stored_number = 0
    # Sumar el número actual al número almacenado
    stored_var.set(stored_number + current_number)
    # Limpiar la caja de texto
    entry.delete(0, tk.END)

def show_result():
    try:
        # Mostrar el número almacenado en la caja de texto
        result_number = int(stored_var.get())
    except ValueError:
        result_number = 0
    text_var.set(result_number)

def clear_all():
    # Limpiar el número almacenado y la caja de texto
    stored_var.set("0")
    text_var.set("0")
    entry.delete(0, tk.END)

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora Suma")
root.geometry("300x200")  # Definir el tamaño de la ventana

# Variables para la caja de texto y el número almacenado
text_var = tk.StringVar()
text_var.set("0")  # Inicializar con 0
stored_var = tk.StringVar()
stored_var.set("0")  # Inicializar con 0

# Crear el botón para sumar el número
add_button = tk.Button(root, text="Sumar", command=add_number)
add_button.grid(row=0, column=0, padx=10, pady=10)

# Crear el botón para mostrar el resultado
equal_button = tk.Button(root, text="Igual", command=show_result)
equal_button.grid(row=0, column=1, padx=10, pady=10)

# Crear el botón para borrar el número
clear_button = tk.Button(root, text="Borrar todo", command=clear_all)
clear_button.grid(row=0, column=2, padx=10, pady=10)

# Crear la caja de texto para ingresar números
entry = tk.Entry(root)
entry.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Crear la caja de texto para mostrar el resultado
result_entry = tk.Entry(root, textvariable=text_var)
result_entry.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Iniciar el bucle principal de la interfaz
root.mainloop()
