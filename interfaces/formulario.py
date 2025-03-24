import customtkinter as ctk
import tkinter.messagebox as messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

janela = ctk.CTk()
janela.title("Tela de Login e Formulário")
janela.geometry("500x450")
janela.resizable(False, False)
janela.iconbitmap("formu.ico") 

#------------------------------

def verificar_login():
    usuario = entrada_user.get()
    senha = entrada_pwd.get()
    
    if usuario == "12" and senha == "34":
        messagebox.showinfo("Login", "O Login foi Bem-Sucedido!")
        formulario()
    else:
        messagebox.showerror("ERRO", "Usuário ou Senha incorretos!")

def formulario():
    label_usuario.pack_forget()
    entrada_user.pack_forget()
    label_senha.pack_forget()
    entrada_pwd.pack_forget()
    botao_login.pack_forget()
    
    label_perguntaUm.pack(pady=10)
    entrada_perguntaUm.pack()
    label_perguntaDois.pack(pady=10)
    entrada_perguntaDois.pack()
    label_perguntaTres.pack(pady=10)
    entrada_perguntaTres.pack()
    label_perguntaQuatro.pack(pady=10)
    entrada_perguntaQuatro.pack()
    botao_enviar.pack(pady=40)

def enviar_formulario():
    messagebox.showinfo("Formulário", "Formulário enviado com sucesso!")
    janela.destroy()

label_usuario = ctk.CTkLabel(janela, text="Usuário:", font=("Arial", 20, "bold"))
label_usuario.pack(pady=20)

entrada_user = ctk.CTkEntry(janela, width=200, font=("Arial", 15))
entrada_user.pack()

label_senha = ctk.CTkLabel(janela, text="Senha:", font=("Arial", 20, "bold"))
label_senha.pack(pady=20)

entrada_pwd = ctk.CTkEntry(janela, width=200, show="*", font=("Arial", 15))
entrada_pwd.pack()

botao_login = ctk.CTkButton(janela, text="LOGIN", font=("Arial", 20, "bold"), command=verificar_login, width=150, height=40)
botao_login.pack(pady=70)

label_perguntaUm = ctk.CTkLabel(janela, text="Qual é o seu nome?", font=("Arial", 14, "bold"))
entrada_perguntaUm = ctk.CTkEntry(janela, width=200, font=("Arial", 14))

label_perguntaDois = ctk.CTkLabel(janela, text="Qual é a sua idade?", font=("Arial", 14, "bold"))
entrada_perguntaDois = ctk.CTkEntry(janela, width=200, font=("Arial", 12))

label_perguntaTres = ctk.CTkLabel(janela, text="Qual é a sua cor favorita?", font=("Arial", 14, "bold"))
entrada_perguntaTres = ctk.CTkEntry(janela, width=200, font=("Arial", 12))

label_perguntaQuatro = ctk.CTkLabel(janela, text="Qual é a sua altura?", font=("Arial", 14, "bold"))
entrada_perguntaQuatro = ctk.CTkEntry(janela, width=200, font=("Arial", 12))

botao_enviar = ctk.CTkButton(janela, text="ENVIAR", font=("Arial", 16, "bold"), command=enviar_formulario)

janela.mainloop()