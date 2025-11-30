import tkinter as tk
from tkinter import messagebox

def abrir_pergunta_genetica():
    janela = tk.Toplevel()
    janela.title("Desafio Genético – Proporções Fenotípicas")
    janela.geometry("400x330")
    janela.resizable(False, False)

    tk.Label(janela, text="Desafio de Genética", font=("Arial", 16, "bold")).pack(pady=10)

    explicacao = (
        "Você receberá um cruzamento e deverá calcular\n"
        "as proporções fenotípicas esperadas.\n"
        "Exemplo: 3:1, 1:2:1, 9:3:3:1..."
    )
    tk.Label(janela, text=explicacao, font=("Arial", 11)).pack(pady=5)

    # --- PERGUNTA DO DESAFIO ---
    cruzamento = "Aa x Aa"   # Você pode trocar depois se quiser
    resposta_correta = "3:1"  # Resultado de Aa x Aa

    tk.Label(janela, text=f"Cruzamento: {cruzamento}", font=("Arial", 14)).pack(pady=10)

    tk.Label(janela, text="Qual a proporção fenotípica esperada?").pack()

    entrada = tk.Entry(janela, font=("Arial", 12))
    entrada.pack(pady=5)

    def verificar():
        resposta = entrada.get().strip().replace(" ", "")

        if resposta == resposta_correta.replace(" ", ""):
            janela.destroy()
            messagebox.showinfo("Resultado", "3 _ _ _")
        else:
            messagebox.showerror("Resultado", f"❌ Resposta incorreta.\n"
                                              f"O correto é: {resposta_correta}")

    tk.Button(
        janela, 
        text="Verificar resposta", 
        font=("Arial", 12), 
        command=verificar
    ).pack(pady=15)

    tk.Label(janela, text="Dica: considere dominância completa.", font=("Arial", 10, "italic")).pack(pady=5)
