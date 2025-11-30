import tkinter as tk
from tkinter import messagebox

def abrir_desafio_mendel():
    janela = tk.Toplevel()
    janela.title("Desafio – Primeira Lei de Mendel")
    janela.geometry("500x420")
    janela.resizable(False, False)

    titulo = tk.Label(
        janela,
        text="Desafio – Primeira Lei de Mendel",
        font=("Arial", 18, "bold")
    )
    titulo.pack(pady=15)

    enunciado = (
        "Considere que o alelo para flor roxa (P) é dominante\n"
        "e o alelo para flor branca (p) é recessivo.\n"
        "No cruzamento PP × pp, qual será o fenótipo dos descendentes?"
    )

    tk.Label(janela, text=enunciado, font=("Arial", 12), justify="center").pack(pady=10)

    alternativas = {
        "A": "100% flores roxas",
        "B": "75% roxas e 25% brancas",
        "C": "50% roxas e 50% brancas",
        "D": "100% flores brancas"
    }

    resposta_correta = "A"  # PP × pp = 100% Pp → todas roxas

    var = tk.StringVar()

    frame_opcoes = tk.Frame(janela)
    frame_opcoes.pack()

    for letra, texto in alternativas.items():
        tk.Radiobutton(
            frame_opcoes,
            text=f"{letra}) {texto}",
            variable=var,
            value=letra,
            font=("Arial", 12)
        ).pack(anchor="w")

    def verificar():
        if var.get() == "":
            messagebox.showwarning("Aviso", "Selecione uma alternativa!")
            return

        if var.get() == resposta_correta:
            janela.destroy()
            messagebox.showinfo("Resultado", "_ _ _ 9")
        else:
            janela.destroy()
            messagebox.showerror(
                "Resultado",
                "❌ Resposta incorreta.\n"
                ""
            )

    tk.Button(janela, text="Verificar Resposta", font=("Arial", 13), command=verificar).pack(pady=20)

    tk.Label(janela, text="Dica: Dominante sempre aparece no fenótipo.", font=("Arial", 10, "italic")).pack()
