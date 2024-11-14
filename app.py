import ttkbootstrap as tk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style
import bd
import os

usuario, satisfacao = '', ''
janela_usuario = None
janela_feedback = None

def aluno_():
    global usuario
    usuario = "aluno"
    janela_usuario.destroy()
    abrir_feedback()

def professor_():
    global usuario
    usuario = "professor"
    janela_usuario.destroy()
    abrir_feedback()

def outros_():
    global usuario
    usuario = "outros"
    janela_usuario.destroy()
    abrir_feedback()

def satisfacao1_():
    global satisfacao
    satisfacao = "satisfacao1"
    bd.verifica(satisfacao, usuario)
    janela_feedback.destroy()
    usuario_()

def satisfacao2_():
    global satisfacao
    satisfacao = "satisfacao2"
    bd.verifica(satisfacao, usuario)
    janela_feedback.destroy()
    usuario_()

def satisfacao3_():
    global satisfacao
    satisfacao = "satisfacao3"
    bd.verifica(satisfacao, usuario)
    janela_feedback.destroy()
    usuario_()

def satisfacao4_():
    global satisfacao
    satisfacao = "satisfacao4"
    bd.verifica(satisfacao, usuario)
    janela_feedback.destroy()
    usuario_()

def satisfacao5_():
    global satisfacao
    satisfacao = "satisfacao5"
    bd.verifica(satisfacao, usuario)
    janela_feedback.destroy()
    usuario_()

def usuario_():
    global usuario
    global janela_usuario
    janela_usuario = tk.Window(themename='litera')
    janela_usuario.state('zoomed')

    opcoes = tk.Frame(janela_usuario, padding=50)
    opcoes.grid(column=1, row=1)
    opcoes.place(relx=0.5, rely=0.5, anchor='center')

    tk.Label(opcoes, text=' Quem é você? ', padding=40).grid(column=1, row=1, columnspan=3)
    tk.Button(opcoes, text="Aluno", command=aluno_).grid(column=1, row=3)
    tk.Button(opcoes, text="Professor", command=professor_).grid(column=2, row=3)
    tk.Button(opcoes, text="Outros", command=outros_).grid(column=3, row=3)

    janela_usuario.title('Usuario')
    janela_usuario.mainloop()

def abrir_feedback():
    global janela_feedback
    janela_feedback = tk.Window(themename='litera')
    janela_feedback.state('zoomed')

    opcoes = tk.Frame(janela_feedback, padding=50)
    opcoes.grid(column=1, row=1)
    opcoes.place(relx=0.5, rely=0.5, anchor='center')

    tk.Label(opcoes, text=' Qual seu nível de satisfação? ', padding=40).grid(column=1, row=1, columnspan=5)
    tk.Button(opcoes, text="\U0001F621", command=satisfacao1_).grid(column=1, row=3)
    tk.Button(opcoes, text="\U0001F641", command=satisfacao2_).grid(column=2, row=3)
    tk.Button(opcoes, text="\U0001F610", command=satisfacao3_).grid(column=3, row=3)
    tk.Button(opcoes, text="\U0001F643", command=satisfacao4_).grid(column=4, row=3)
    tk.Button(opcoes, text="\U0001F60A", command=satisfacao5_).grid(column=5, row=3)

    janela_feedback.title('Satisfação')
    janela_feedback.mainloop()

def main():
    global usuario, satisfacao
    usuario = None
    satisfacao = None
    usuario_()

if __name__ == '__main__':
    main()
