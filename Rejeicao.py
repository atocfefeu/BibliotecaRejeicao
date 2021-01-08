from tkinter import *
import conexao_sql
import pyodbc

root = Tk()
root.geometry("600x300")
root.title('Rejeicao NFCe/NFe')

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 20
        self.primeiroContainer.pack()

        self.fontePadrao = ("Arial", "10")
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 10
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="BIBLIOTECA DE REJEIÇÕES NF-e/NFC-e")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.configure(relief="ridge")
        self.titulo.pack()

        self.numeroLabel = Label(self.segundoContainer, text="Digite o código:", font=self.fontePadrao)
        self.numeroLabel.pack(side=LEFT)

        self.numero = Entry(self.segundoContainer)
        self.numero["width"] = 10
        self.numero["font"] = self.fontePadrao
        self.numero.pack(side=LEFT)

        self.autenticar = Button(self.terceiroContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

        self.mensagem1 = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem1.pack()

        self.mensagem2 = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem2.pack()
    # Método verificar senha
    def verificaSenha(self):
        number = self.numero.get()
        cursor = conexao_sql.retornar_conexao_sql()
        if cursor.execute(f'SELECT Motivo FROM tbl_Rejeicao WHERE Código = {number}'):
            query = cursor.fetchall()
            self.mensagem["text"] = "Motivo:",query[0]

            if cursor.execute(f'SELECT Causa FROM tbl_Rejeicao WHERE Código = {number}'):
                query = cursor.fetchall()
                self.mensagem1["text"] = "Causa:",query[0]

                if cursor.execute(f'SELECT Solução FROM tbl_Rejeicao WHERE Código = {number}'):
                    query = cursor.fetchall()
                    self.mensagem2["text"] = query[0]
        else:
            self.mensagem["text"] = "Não encontrado"


'''
cursor = retornar_conexao_sql()
cursor.execute("SELECT Solução FROM tbl_Rejeicao WHERE Código = 206")
row = cursor.fetchone()
if row:
    print(row)
    '''
Application(root)
root.mainloop()