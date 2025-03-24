import customtkinter as ctk
import tkinter.messagebox as messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

janela = ctk.CTk()
janela.title("App saúde")
janela.geometry("500x250")
janela.resizable(False, False)

#------------------------------

def clique():
    try:
        peso = float(campoPeso.get())
        altura = float(campoAltura.get())
        imc = peso / (altura ** 2)
        messagebox.showinfo('Resultado', f'Seu IMC é: {imc:.2f}')
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

ctk.CTkLabel(janela, 
             text='App Saúde 2024',
             text_color='red',
             font=('Arial', 30, 'bold')).pack(pady=10)

campoPeso = ctk.CTkEntry(janela, 
                         width=200, 
                         height=40,
                         placeholder_text="Informe seu peso: ")
campoPeso.pack(pady=10)

campoAltura = ctk.CTkEntry(janela, 
                           width=200, 
                           height=40,
                           placeholder_text="Informe sua altura: ")
campoAltura.pack(pady=10)

botao = ctk.CTkButton(janela, 
                      width=100,
                      height=30,
                      text="Calcular",
                      font=('Arial', 20, 'bold'),
                      fg_color='red',
                      command=clique)
botao.pack(pady=10)

resultadoImc = ctk.CTkLabel(janela, 
                            text=' ', 
                            text_color="white", 
                            font=("Arial", 30))
resultadoImc.pack(pady=30)

janela.mainloop()