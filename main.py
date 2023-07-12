from tkinter import *


janela = Tk()

class Funcs:
  def limpa_tela(self):
    self.entry_data.delete(0, END)
    self.entry_entrada.delete(0, END)
    self.entry_saida.delete(0, END)

  def cadastrar_horario(self):
    self.data = self.entry_data.get()
    self.entrada = self.entry_entrada.get()
    self.saida = self.entry_saida.get()

    with open('frequencia.txt', 'a') as arquivo:
      #arquivo.write('data' + ';' + 'entrada' + ';' + 'saída' + '\n')
      arquivo.write(self.data + ';' + self.entrada + ';' + self.saida + '\n')
    self.limpa_tela()

class Frequencia(Funcs):
  def __init__(self):
    self.janela = janela
    self.config_tela()
    self.label_tela()
    self.criar_botao()

    janela.mainloop()

  def config_tela(self):
    self.janela.title('Registro de Frequência')
    self.janela.geometry('350x200')
    self.janela.config(bg='#F2F3F4')
    self.janela.resizable(False, False)

  def label_tela(self):
    self.lb_data = Label(self.janela, text='Data', bg='#F2F3F4', font=('Arial 10 bold'))
    self.lb_data.place(relx=0.01, rely=0.01)
    self.entry_data = Entry(self.janela)
    self.entry_data.place(relx=0.01, rely=0.11, relwidth=0.3)

    self.lb_entrada = Label(self.janela, text='Entrada', bg='#F2F3F4', font=('Arial 10 bold'))
    self.lb_entrada.place(relx=0.01, rely=0.31)
    self.entry_entrada = Entry(self.janela)
    self.entry_entrada.place(relx=0.01, rely=0.41, relwidth=0.3)

    self.lb_saida = Label(self.janela, text='Saída', bg='#F2F3F4', font=('Arial 10 bold'))
    self.lb_saida.place(relx=0.50, rely=0.31)
    self.entry_saida = Entry(self.janela)
    self.entry_saida.place(relx=0.50, rely=0.41, relwidth=0.3)

  def criar_botao(self):
    self.bt_cadastrar = Button(self.janela, text='Cadastrar', font=('Arial 10 bold'), command=self.cadastrar_horario)
    self.bt_cadastrar.place(relx=0.35, rely=0.65)
    



Frequencia()