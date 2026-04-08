"""
Componentes Basicos de Tkinter
Tinker(): ventana principal
Label(): Muestra texto o imagenes
Entry(): Campo de texto
Button(): Boton interactivo
Text(): campo de texto multilinea
Frame: cibteberdir oara agrupar otros widgets
LIstbox, Checkbutton, Radiobutton, Canvas, entre otros


Atributos comunes:
text: texto del componente
wigth, heaight: dimensiones
bg, fg: colores de fondo y texti
font: tipo y tamanio de fuente
command: funciona al ejecutar al interactuar con el widget
pack(), grid(), place(): metodos de posicionamiento

"""

# Ejecutar en consola
# pip install tkinter

import tkinter as tk

def saludar():
    #Entrada es la caja de texto y .get() es capturar lo que este digitado
    nombre = entrada.get()
    
    #para cambiar un atributo del componente utilizar .config()
    #carga lo escrito en la caja de texto en la etiqueta_saliudo
    etiqueta_saludo.config(text=f'Hola {nombre}, bienvenido!')
    
if __name__ == "__main__":
    #Creamos la ventana, en este caso se la asignamos a la variable ventana
    formulario = tk.Tk()
    #Le configuramos un titulo a la ventana, se mostrara en la esquina superior izq de la ventana
    formulario.title("Ejemplo con Tkinter")
    
    #Ahora cargamos una etiqueta dentro de la ventana
    #Los parametros del label son: formulario donde cargar el label, y un texto para el usuario
    etiqueta = tk.Label(formulario, text= "Ingresa tu nombre: ")
    #para cargarlo en la ventana vamos a usar .pack() en el componente, esto hace que se 
    # coloque un componente encima/sobre otro
    etiqueta.pack()
    
    #vamos a crear una caja de texto, se conocen como entrada en tkinter
    entrada = tk.Entry(formulario)
    entrada.pack()
    
    #Ahora un boton, los parametros son: formulario donde cargar, texto al usuario
    # y la Funcion a INVOCAR cuando se presiona
    boton = tk.Button(formulario,text="Saludar", command=saludar)
    boton.pack()
    
    #Al inicializar el programa la etiqueta se carga vacia
    etiqueta_saludo = tk.Label(formulario, text="")
    etiqueta_saludo.pack()
    
    ##abrimos el formulario con toda su configuracion
    formulario.mainloop()