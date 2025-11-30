import tkinter as tk
import time
from tkinter import PhotoImage
import pygame

pygame.mixer.init()
pygame.mixer.music.load("img/videoplayback-_3_.wav")


# Tocar som uma vez

# Tocar em loop até parar
# winsound.PlaySound("som.wav", winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)


# Para tocar em loop:
# pygame.mixer.music.play(-1)


def criar_area_de_trabalho():
    root = tk.Toplevel()
    root.title("Lixeira")
    root.geometry("900x525")
    root.resizable(False, False)

    canvas = tk.Canvas(root, width=900, height=525, highlightthickness=0, bg="#a0a0a0")
    canvas.pack(fill="both", expand=True)

    # --------------------- ÍCONES --------------------- #
    folder_icon = tk.PhotoImage(file="img/mp4.png").subsample(7,7)
    
    # Criando o ícone de folder clicável
    exeapp = canvas.create_image(70, 80, image=folder_icon)
    canvas.tag_bind(exeapp, "<Button-1>", lambda e: abrir_filho())
    exetext = canvas.create_text(70, 130, text="Click_me.mp4", fill="white", font=("Segoe UI", 12))
    canvas.tag_bind(exetext, "<Button-1>", lambda e: abrir_filho())

    # --------------------- FUNÇÃO PARA ABRIR FOLDER --------------------- #
    def abrir_filho():
        global filho
        filho = tk.Toplevel(root)
        filho.title("Folder")
        filho.geometry("300x200")
        filho.resizable(False, False)
        filho.config(bg="white")

        # Carregar GIF
        gif = tk.PhotoImage(file="img/rickroll.gif")

        # Criar label e manter referência do GIF
        label = tk.Label(filho, image=gif)
        label.image = gif
        label.pack(pady=10)
        pygame.mixer.music.play()
        

    root.mainloop()
criar_area_de_trabalho()