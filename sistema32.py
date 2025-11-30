import tkinter as tk
from tkinter import ttk
import desktop

def abrir_desktop():
    root.destroy()
    desktop.abrir() 
# -----------------------------------------------------
# JANELA PRINCIPAL
# -----------------------------------------------------
root = tk.Tk()
root.title("Login Windows Style")
root.geometry("900x525")
root.resizable(False, False)

# -----------------------------------------------------
# CANVAS PRINCIPAL
# -----------------------------------------------------
canvas = tk.Canvas(root, width=900, height=525, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# -----------------------------------------------------
# FUNDO COM IMAGEM CENTRALIZADA
# -----------------------------------------------------
# IMPORTANTE: Tkinter NÃO aceita JPG -> use PNG ou GIF

fundo = tk.PhotoImage(file="img/fundo.png").subsample(2, 2)  
# subsample(2,2) reduz de 1920x1080 → 960x540 (cabe melhor)

canvas.update()
cx = canvas.winfo_width() // 2
cy = canvas.winfo_height() // 2

canvas.create_image(cx, cy, image=fundo, anchor="center")

# -----------------------------------------------------
# AVATAR (círculo branco + imagem)
# -----------------------------------------------------
avatar_size = 120
x_center = 450

# Círculo branco
canvas.create_oval(
    x_center - avatar_size / 2,
    180,
    x_center + avatar_size / 2,
    180 + avatar_size,
    fill="white",
    outline=""
)

# Avatar (use PNG!)
img = tk.PhotoImage(file="img/download.png").subsample(2, 2)

# Centralizar dentro do círculo
canvas.create_image(
    x_center,
    180 + avatar_size // 2,
    image=img,
    anchor="center"
)

# -----------------------------------------------------
# NOME DO USUÁRIO
# -----------------------------------------------------
canvas.create_text(
    x_center,
    330,
    text="Bob Necromante",
    font=("Segoe UI", 30),
    fill="white"
)

# -----------------------------------------------------
# CAMPO DE SENHA
# -----------------------------------------------------
senha_var = tk.StringVar()

senha_entry = ttk.Entry(
    root,
    textvariable=senha_var,
    font=("Segoe UI", 18),
    show="*"
)

senha_box = canvas.create_window(
    x_center,
    390,
    window=senha_entry,
    width=280,
    height=40
)

# -----------------------------------------------------
# FUNÇÃO DE LOGIN
# -----------------------------------------------------
def login():
    if(senha_var.get() == "bobao"):
       abrir_desktop()

# -----------------------------------------------------
# BOTÃO DE ENTRAR (→)
# -----------------------------------------------------
botao = ttk.Button(root, text="→", command=login)

botao_box = canvas.create_window(
    x_center + 150,
    390,
    window=botao,
    width=50,
    height=40
)

# -----------------------------------------------------
# FECHAR COM ESC
# -----------------------------------------------------
root.bind("<Escape>", lambda e: root.destroy())

root.mainloop()
