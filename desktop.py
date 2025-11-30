import tkinter as tk
import genetica
import desafio_genetico
import punnett
import mendel_desafio
import time

def abrir():
    root = tk.Tk()
    root.title("Windows Desktop")
    root.geometry("900x525")
    root.resizable(False, False)

    canvas = tk.Canvas(root, width=900, height=525, highlightthickness=0, bg="#000000")
    canvas.pack(fill="both", expand=True)

    # -----------------------------------------------------
    # PAPEL DE PAREDE
    # -----------------------------------------------------
    wallpaper = tk.PhotoImage(file="img/vapor.png")

    canvas.update()
    cx = canvas.winfo_width() // 2
    cy = canvas.winfo_height() // 2

    canvas.create_image(cx, cy, image=wallpaper, anchor="center")

    # -----------------------------------------------------
    # ÍCONES
    # -----------------------------------------------------
    folder = tk.PhotoImage(file="img/exe.png").subsample(9, 9)
    trash = tk.PhotoImage(file="img/trash.png").subsample(9, 9)

    exeapp = canvas.create_image(70, 80, image=folder)
    canvas.tag_bind(exeapp, "<Button-1>", lambda e: abrir_filho())
    exetext = canvas.create_text(70, 130, text="Senha_cofre.exe", fill="white", font=("Segoe UI", 12))
    canvas.tag_bind(exetext, "<Button-1>", lambda e: abrir_filho())
    
    def abrir_filho():
        global filho
        filho = tk.Toplevel(root)
        filho.title("Senha_cofre.exe")
        filho.geometry("300x200")
        filho.resizable(False, False)
        filho.config(bg="white")  # opcional: fundo branco
        
        label = tk.Label(filho, text="Digite algo e pressione o botao Enter")
        label.pack(pady=5)

        # Caixa de texto
        global texto
        texto = tk.StringVar()
        entrada = tk.Entry(filho, width=30, textvariable=texto)
        entrada.pack(pady=5)
        entrada.focus()
        button = tk.Button(filho, command=pergunta, text="Enter").pack(pady=5)

    def pergunta():
        if(texto.get() == "eu te amo"):
            filho.destroy()
            genetica.abrir_pergunta_genetica()
        if(texto.get() == "voce me ama"):
            filho.destroy()
            desafio_genetico.abrir_desafio_genetico()
        if(texto.get() == "nao amo"):
            filho.destroy()
            punnett.abrir_desafio_punnett()
        if(texto.get() == "amo"):
            filho.destroy()
            mendel_desafio.abrir_desafio_mendel()
        
    canvas.create_image(70, 190, image=trash)
    canvas.create_text(70, 240, text="Lixeira", fill="white", font=("Segoe UI", 12))

    # -----------------------------------------------------
    # BARRA DE TAREFAS
    # -----------------------------------------------------
    canvas.create_rectangle(0, 485, 900, 525, fill="#202020", outline="")

    start_icon = tk.PhotoImage(file="img/download.png").subsample(5, 5)
    canvas.create_image(30, 505, image=start_icon)

    # -----------------------------------------------------
    # RELÓGIO
    # -----------------------------------------------------
    clock = canvas.create_text(860, 505, text="00:00", fill="white",
                               font=("Segoe UI", 12, "bold"))

    def atualizar_relogio():
        canvas.itemconfig(clock, text=time.strftime("%H:%M"))
        root.after(1000, atualizar_relogio)

    atualizar_relogio()

    root.mainloop()