import tkinter as tk
from tkinter import messagebox

class TelaLogin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        
        self.rotulo_usuario = tk.Label(self, text="Usuário:")
        self.rotulo_usuario.pack()
        self.entrada_usuario = tk.Entry(self)
        self.entrada_usuario.pack()
        
        self.rotulo_senha = tk.Label(self, text="Senha:")
        self.rotulo_senha.pack()
        self.entrada_senha = tk.Entry(self, show="*")
        self.entrada_senha.pack()
        
        self.check_lembrar_senha = tk.Checkbutton(self, text="Lembrar senha")
        self.check_lembrar_senha.pack()
        
        self.botao_login = tk.Button(self, text="Login", command=self.login)
        self.botao_login.pack()

    def login(self):
        usuario = self.entrada_usuario.get()
        senha = self.entrada_senha.get()
        
        # Verificar se o login está correto
        if usuario == "usuario" and senha == "senha":
            self.destroy()  # Fecha a tela de login
            self.mostrar_menu_principal()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos")

    def mostrar_menu_principal(self):
        menu_principal = MenuPrincipal()
        menu_principal.mainloop()

class MenuPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Menu Principal")

        self.rotulo = tk.Label(self, text="Selecione um objeto:")
        self.rotulo.pack()

        self.botao_brocas = tk.Button(self, text="Brocas", command=self.mostrar_menu_brocas)
        self.botao_brocas.pack()

        self.botao_machos = tk.Button(self, text="Machos", command=self.mostrar_menu_machos)
        self.botao_machos.pack()

    def mostrar_menu_brocas(self):
        menu_brocas = MenuObjeto("Brocas", ["Brocas Novas", "Brocas em Afiação", "Brocas Afiadas"])
        menu_brocas.mainloop()

    def mostrar_menu_machos(self):
        menu_machos = MenuObjeto("Machos", ["Machos Novos", "Machos em Afiação", "Machos Afiados"])
        menu_machos.mainloop()

class MenuObjeto(tk.Tk):
    def __init__(self, tipo_objeto, opcoes):
        super().__init__()
        self.title(f"{tipo_objeto}")

        self.rotulo = tk.Label(self, text=f"Selecione o tipo de {tipo_objeto}:")
        self.rotulo.pack()

        for opcao in opcoes:
            botao = tk.Button(self, text=opcao)
            botao.pack()

if __name__ == "__main__":
    tela_login = TelaLogin()
    tela_login.mainloop()