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
    cruzamento = "Aa x aa"
    tk.Label(janela, text=f"Cruzamento: {cruzamento}", font=("Arial", 14)).pack(pady=10)

    tk.Label(janela, text="Qual a proporção fenotípica esperada?").pack()

    entrada = tk.Entry(janela, font=("Arial", 12))
    entrada.pack(pady=5)

    def verificar():
        resposta = entrada.get().strip().replace(" ", "")

        # Verifica se está no formato correto X:X
        if ":" in resposta:
            partes = resposta.split(":")

            # Verifica se os dois lados são números
            if len(partes) == 2 and partes[0].isdigit() and partes[1].isdigit():

                a = int(partes[0])
                b = int(partes[1])

                # Se os números forem iguais → está correto
                if a == b:
                    janela.destroy()
                    messagebox.showinfo("Resultado", "3 _ _ _")
                    return

        # Se chegou aqui → incorreta
        janela.destroy()
        messagebox.showerror(
            "Resultado",
            f"❌ Resposta incorreta.\n"
            f""
        )


    tk.Button(
        janela, 
        text="Verificar resposta", 
        font=("Arial", 12), 
        command=verificar
    ).pack(pady=15)
    tk.Label(janela, text="Dica: considere dominância completa.", font=("Arial", 10, "italic")).pack(pady=5)
