# se importan las funciones definidas anteriormente para 
# implementarlas en la interfaz de customthinker
import customtkinter as ctk
import logica_juego1 as l1
from PIL import Image


# funcion que muestra la imagen que se genero (se ejecuta solamente, pero no retorna nada)
def actualizar_imagen(label_donde_mostrar)->None:
    imagen_generada = l1.choise_image()
    
    # se procesa la imagen con pillow
    img_pil = Image.open(imagen_generada)
    # ajuste de tamaño
    img_ajustada = ctk.CTkImage(light_image=img_pil, size=(250, 250))
    # se actualiza el widget que ya existe
    label_donde_mostrar.configure(image=img_ajustada, text="")
    # evita que python borre la imagen de la ram
    label_donde_mostrar.image = img_ajustada


ventana_juego1 = ctk.CTk()
ventana_juego1.geometry("400x450")
ventana_juego1.title("Visor de Señas Aleatorio")
# abajo de la creacion de la ventana se pueden definir otras caracteristicas como la dimension de la ventana, los colores, elementos. etc.






# Ejecuta el programa hasta que el usuario lo cierre
ventana_juego1.mainloop()




# letras = ["A", "e", "i"]

#    i  = 0
#    for i < 3: