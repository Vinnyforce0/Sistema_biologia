import tkinter as tk
from tkinter import messagebox

def abrir_desafio_punnett():
    janela = tk.Toplevel()
    janela.title("Desafio – Interpretar Quadro de Punnett")
    janela.geometry("520x480")
    janela.resizable(False, False)

    tk.Label(
        janela, 
        text="Desafio: Interpretar um quadro de Punnett", 
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    descricao = (
        "Abaixo está um quadro de Punnett para o cruzamento:\n"
        "Aa  ×  Aa\n\n"
        "Use o quadro para descobrir a proporção\n"
        "fenotípica esperada (dominância simples)."
    )
    tk.Label(janela, text=descricao, font=("Arial", 11)).pack(pady=5)

    # ------------------- QUADRO DE PUNNETT ------------------- #
    quadro = tk.Frame(janela, bd=2, relief="solid")
    quadro.pack(pady=15)

    # Rótulos de topo (gametas)
    tk.Label(quadro, text="", width=8, height=2).grid(row=0, column=0)
    tk.Label(quadro, text="A", width=8, height=2, bg="#ddeaff").grid(row=0, column=1)
    tk.Label(quadro, text="a", width=8, height=2, bg="#ddeaff").grid(row=0, column=2)

    # Linha 1
    tk.Label(quadro, text="A", width=8, height=2, bg="#ddeaff").grid(row=1, column=0)
    tk.Label(quadro, text="AA", width=8, height=2).grid(row=1, column=1)
    tk.Label(quadro, text="Aa", width=8, height=2).grid(row=1, column=2)

    # Linha 2
    tk.Label(quadro, text="a", width=8, height=2, bg="#ddeaff").grid(row=2, column=0)
    tk.Label(quadro, text="Aa", width=8, height=2).grid(row=2, column=1)
    tk.Label(quadro, text="aa", width=8, height=2).grid(row=2, column=2)
    # ----------------------------------------------------------- #

    # Proporção fenotípica esperada para Aa × Aa (dominância completa):
    proporcao_correta = "3:1"

    tk.Label(janela, text="Qual é a proporção fenotípica esperada? (3:1, 1:2:1, etc...)", font=("Arial", 12)).pack()

    entrada = tk.Entry(janela, font=("Arial", 12), width=10)
    entrada.pack(pady=5)

    def verificar():
        resp = entrada.get().strip().replace(" ", "")
        if resp == proporcao_correta.replace(" ", ""):
            janela.destroy()
            messagebox.showinfo("Resultado", "_ _ 5 _")
        else:
            messagebox.showerror("Erro",
                f"❌ Resposta incorreta.\nO correto é: {proporcao_correta}"
            )

    tk.Button(
        janela,
        text="Verificar resposta",
        font=("Arial", 12),
        command=verificar
    ).pack(pady=10)

    tk.Label(
        janela, 
        text="Dica: A = dominante | a = recessivo", 
        font=("Arial", 10, "italic")
    ).pack()
