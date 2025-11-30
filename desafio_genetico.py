import tkinter as tk
from tkinter import messagebox
import random

# ==========================================================
# LISTA DE DESAFIOS (perguntas + resposta correta)
# ==========================================================
DESAFIOS = [
    {
        "pergunta": "1) Cruzamento: Aa × aa\nQual a probabilidade (%) de descendentes recessivos?",
        "resposta": 50
    },
    {
        "pergunta": "2) Cruzamento: Aa × Aa\nQual a probabilidade (%) de descendentes recessivos?",
        "resposta": 25
    },
    {
        "pergunta": "3) Cruzamento: BB × Bb\nQual a probabilidade (%) de descendentes recessivos?",
        "resposta": 0
    },
    {
        "pergunta": "4) Cruzamento: AaBb × aabb\nProbabilidade (%) do descendente ser totalmente recessivo?",
        "resposta": 25
    },
    {
        "pergunta": "5) Cruzamento: Aa × AA\nQual a probabilidade (%) de descendentes dominantes?",
        "resposta": 100
    }
]

# ==========================================================
# FUNÇÃO PRINCIPAL – ABRE A PÁGINA DO DESAFIO
# ==========================================================
def abrir_desafio_genetico():

    # ------------------------------------------------------
    # Função interna: verifica resposta
    # ------------------------------------------------------
    def verificar_resposta():
        resposta = entrada.get().replace("%", "").strip()

        try:
            valor = float(resposta)
        except:
            messagebox.showerror("Erro", "Digite um número válido!")
            return

        if abs(valor - desafio["resposta"]) < 0.1:
            janela.destroy()
            messagebox.showinfo("Resultado", "_ 8 _ _")
        else:
            messagebox.showwarning(
                "Resultado",
                f"❌ Incorreto!\nA resposta certa é {desafio['resposta']}%."
            )

    # ------------------------------------------------------
    # Seleciona desafio aleatório
    # ------------------------------------------------------
    desafio = random.choice(DESAFIOS)

    # ------------------------------------------------------
    # JANELA FILHA (Toplevel)
    # ------------------------------------------------------
    janela = tk.Toplevel()
    janela.title("Desafio de Cruzamento Genético")
    janela.geometry("550x350")
    janela.resizable(False, False)

    # Título
    titulo = tk.Label(janela, text="🔬 Desafio: Cruzamento Genético",
                      font=("Segoe UI", 18, "bold"))
    titulo.pack(pady=15)

    # Texto da pergunta
    pergunta_label = tk.Label(janela, text=desafio["pergunta"],
                              font=("Segoe UI", 14),
                              justify="center")
    pergunta_label.pack(pady=10)

    # Entrada do aluno
    entrada = tk.Entry(janela, font=("Segoe UI", 16), justify="center")
    entrada.pack(pady=15)

    # Botão de verificar resposta
    botao = tk.Button(janela, text="Verificar Resposta",
                      font=("Segoe UI", 12),
                      command=verificar_resposta)
    botao.pack(pady=10)

    janela.mainloop()


# ----------------------------------------------------------
# Executa sozinho (se rodar o arquivo direto)
# ----------------------------------------------------------
if __name__ == "__main__":
    abrir_desafio_genetico()
