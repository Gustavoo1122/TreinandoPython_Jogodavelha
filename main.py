from tkinter import *
from tkinter import Tk
from tkinter import messagebox


#Cores do programa
cor1 = '#d6d6d6' #Cinza claro
cor2 = '#c20a0a' #Vermelho
cor3 = '#1510ad' #Azul
cor4 = '#080a29' #Azul escuro
cor5 = '#ffffff' #branco
cor6 = '#000000' #preto


#Criando a janela do programa
janela = Tk()
janela.title('Jogo da Velha')
janela.geometry('700x640')
janela.minsize(700, 640)
janela.maxsize(700, 640)
janela.config(bg = cor4)


#Variáves das casas do tabuleiro
c1 = ''
c2 = ''
c3 = ''
c4 = ''
c5 = ''
c6 = ''
c7 = ''
c8 = ''
c9 = ''


#Variável para definir a vez dos jogadores
rodada = 0

jogador_ganhou = 0

#Função para voltar o menu
def reiniciairtudo():
    ir_menu()

    global c1, c2, c3, c4, c5, c6, c7, c8, c9
    global jogador_ganhou, rodada
    #Desativa os botões do jogador 1
    btn_x1.config(state = DISABLED)
    btn_x2.config(state = DISABLED)
    btn_x3.config(state = DISABLED)
    btn_x4.config(state = DISABLED)
    btn_x5.config(state = DISABLED)
    btn_x6.config(state = DISABLED)
    btn_x7.config(state = DISABLED) 
    btn_x8.config(state = DISABLED)
    btn_x9.config(state = DISABLED)

    #Desativa os botões do jogador 2
    btn_o1.config(state = DISABLED)
    btn_o2.config(state = DISABLED)
    btn_o3.config(state = DISABLED)
    btn_o4.config(state = DISABLED)
    btn_o5.config(state = DISABLED)
    btn_o6.config(state = DISABLED)
    btn_o7.config(state = DISABLED) 
    btn_o8.config(state = DISABLED)
    btn_o9.config(state = DISABLED)

    #Ativa os botões de escolha de quem começa
    btn_escolha1.config(state = NORMAL)
    btn_escolha2.config(state = NORMAL)

    #Limpa as variáveis
    c1 = ''
    c2 = ''
    c3 = ''
    c4 = ''
    c5 = ''
    c6 = ''
    c7 = ''
    c8 = ''
    c9 = ''

    jogador_ganhou = 0
    rodada = 0

    #Limpa o tabuleiro
    casa1Label.config(text = c1)
    casa2Label.config(text = c2)
    casa3Label.config(text = c3)
    casa4Label.config(text = c4)
    casa5Label.config(text = c5)
    casa6Label.config(text = c6)
    casa7Label.config(text = c7)
    casa8Label.config(text = c8)
    casa9Label.config(text = c9)


#Funções para trocar de tela
def ir_jogo():
    frame_Menu.pack_forget()
    frame_Jogo.pack()

def ir_menu():
    frame_Jogo.pack_forget()
    frame_Menu.pack()


#Função para verificar se tem um ganhador
def verifica_ganhador():
    global jogador_ganhou
    #Verifica se o jogador 1 ganhou na horizontal
    if c1 == 'X' and c2 == 'X' and c3 == 'X':
        messagebox.showinfo(title = 'Jogador 1 ganhou', message = 'O jogador 1 ganhou, parabéns!')
        jogador_ganhou = 3
        reiniciairtudo()
        return jogador_ganhou

    elif c4 == 'X' and c5 == 'X' and c6 == 'X':
        messagebox.showinfo(title = 'Jogador 1 ganhou', message = 'O jogador 1 ganhou, parabéns!') 
        jogador_ganhou = 3
        reiniciairtudo()
        return jogador_ganhou

    elif c7 == 'X' and c8 == 'X' and c9 == 'X':
        messagebox.showinfo(title = 'Jogador 1 ganhou', message = 'O jogador 1 ganhou, parabéns!')
        jogador_ganhou = 3
        reiniciairtudo()
        return jogador_ganhou


    #Verifica se o jogador 1 ganhou na vertical
    elif c1 == 'X' and c4 == 'X' and c7 == 'X':
        messagebox.showinfo(title = 'Jogador 1 ganhou', message = 'O jogador 1 ganhou, parabéns!')
        jogador_ganhou = 3
        reiniciairtudo()
        return jogador_ganhou

    elif c2 == 'X' and c5 == 'X' and c8 == 'X':
        messagebox.showinfo(title = 'Jogador 1 ganhou', message = 'O jogador 1 ganhou, parabéns!')
        jogador_ganhou = 3
        reiniciairtudo()
        return jogador_ganhou

    elif c3 == 'X' and c6 == 'X' and c9 == 'X':
        messagebox.showinfo(title = 'Jogador 1 ganhou', message = 'O jogador 1 ganhou, parabéns!')
        jogador_ganhou = 3
        reiniciairtudo()
        return jogador_ganhou

    #Verifica se o jogador 1 ganhou na diagonal
    elif c1 == 'X' and c5 == 'X' and c9 == 'X':
        messagebox.showinfo(title = 'Jogador 1 ganhou', message = 'O jogador 1 ganhou, parabéns!')
        jogador_ganhou = 3
        reiniciairtudo()
        return jogador_ganhou

    elif c3 == 'X' and c5 == 'X' and c7 == 'X':
        messagebox.showinfo(title = 'Jogador 1 ganhou', message = 'O jogador 1 ganhou, parabéns!')
        jogador_ganhou = 3
        reiniciairtudo()
        return jogador_ganhou
    
    
    #Verifica se o jogador 2 ganhou na horizontal
    elif c1 == 'O' and c2 == 'O' and c3 == 'O':
        messagebox.showinfo(title = 'Jogador 2 ganhou', message = 'O jogador 2 ganhou, parabéns!')
        jogador_ganhou = 3
        reiniciairtudo()
        return jogador_ganhou

    elif c4 == 'O' and c5 == 'O' and c6 == 'O':
        messagebox.showinfo(title = 'Jogador 2 ganhou', message = 'O jogador 2 ganhou, parabéns!')
        jogador_ganhou = 3
        reiniciairtudo()
        return jogador_ganhou

    elif c7 == 'O' and c8 == 'O' and c9 == 'O':
        messagebox.showinfo(title = 'Jogador 2 ganhou', message = 'O jogador 2 ganhou, parabéns!')
        jogador_ganhou = 3
        reiniciairtudo()
        return jogador_ganhou

    #Verifica se o jogador 2 ganhou na vertical
    elif c1 == 'O' and c4 == 'O' and c7 == 'O':
        messagebox.showinfo(title = 'Jogador 2 ganhou', message = 'O jogador 2 ganhou, parabéns!')
        jogador_ganhou = 3
        reiniciairtudo()
        return jogador_ganhou

    elif c2 == 'O' and c5 == 'O' and c8 == 'O':
        messagebox.showinfo(title = 'Jogador 2 ganhou', message = 'O jogador 2 ganhou, parabéns!')
        jogador_ganhou = 3
        reiniciairtudo()
        return jogador_ganhou

    elif c3 == 'O' and c6 == 'O' and c9 == 'O':
        messagebox.showinfo(title = 'Jogador 2 ganhou', message = 'O jogador 2 ganhou, parabéns!')
        jogador_ganhou = 3
        reiniciairtudo()
        return jogador_ganhou

    #Verifica se o jogador 2 ganhou na diagonal
    elif c1 == 'O' and c5 == 'O' and c9 == 'O':
        messagebox.showinfo(title = 'Jogador 2 ganhou', message = 'O jogador 2 ganhou, parabéns!')
        jogador_ganhou = 3
        reiniciairtudo()
        return jogador_ganhou

    elif c3 == 'O' and c5 == 'O' and c7 == 'O':
        messagebox.showinfo(title = 'Jogador 2 ganhou', message = 'O jogador 2 ganhou, parabéns!')
        jogador_ganhou = 3  
        reiniciairtudo()
        return jogador_ganhou
    
    #Verifica se deu velha
    elif c1 != '' and c2 != '' and c3 != '' and c4 != '' and c5 != '' and c6 != '' and c7 != '' and c8 != '' and c9 != '':
        messagebox.showinfo(title = 'Deu empate', message = 'O jogo empatou, joguem novamente.')
        reiniciairtudo()


#Função de rodadas
def rodadas_jogo():
    global rodada
    global jogador_ganhou
    
    if rodada == 1:
        vezjogador2()
    elif rodada == 2:
        vezjogador1()


#Funções das jogadas
def jogadaCasa1(e):
    global c1
    global rodada

    if c1 == '':
        if e == 'X':
            c1 = 'X'
            casa1Label.config(text = c1)
            casa1Label.config(fg = cor2)
            rodada = 1
            
        else:
            c1 = 'O'
            casa1Label.config(text = c1)
            casa1Label.config(fg = cor3)
            rodada = 2
        verifica_ganhador()
        rodadas_jogo()

    else:
        messagebox.showerror(title = 'Erro', message = 'Essa casa já está ocupada, escolha outra.')

    return rodada

def jogadaCasa2(e):
    global c2
    global rodada

    if c2 == '':
        if e == 'X':
            c2 = 'X'
            casa2Label.config(text = c2)
            casa2Label.config(fg = cor2)
            rodada = 1
        else:
            c2 = 'O'
            casa2Label.config(text = c2)
            casa2Label.config(fg = cor3)
            rodada = 2
        verifica_ganhador()
        rodadas_jogo()
    else:
        messagebox.showerror(title = 'Erro', message = 'Essa casa já está ocupada, escolha outra.')

    return rodada

def jogadaCasa3(e):
    global c3
    global rodada

    if c3 == '':
        if e == 'X':
            c3 = 'X'
            casa3Label.config(text = c3)
            casa3Label.config(fg = cor2)
            rodada = 1
        else:
            c3 = 'O'
            casa3Label.config(text = c3)
            casa3Label.config(fg = cor3)
            rodada = 2
        verifica_ganhador()
        rodadas_jogo()
    else:
        messagebox.showerror(title = 'Erro', message = 'Essa casa já está ocupada, escolha outra.')

    return rodada

def jogadaCasa4(e):
    global c4
    global rodada

    if c4 == '':
        if e == 'X':
            c4 = 'X'
            casa4Label.config(text = c4)
            casa4Label.config(fg = cor2)
            rodada = 1
        else:
            c4 = 'O'
            casa4Label.config(text = c4)
            casa4Label.config(fg = cor3)
            rodada = 2
        verifica_ganhador()
        rodadas_jogo()
    else:
        messagebox.showerror(title = 'Erro', message = 'Essa casa já está ocupada, escolha outra.')

    return rodada

def jogadaCasa5(e):
    global c5
    global rodada

    if c5 == '':
        if e == 'X':
            c5 = 'X'
            casa5Label.config(text = c5)
            casa5Label.config(fg = cor2)
            rodada = 1
        else:
            c5 = 'O'
            casa5Label.config(text = c5)
            casa5Label.config(fg = cor3)
            rodada = 2
        verifica_ganhador()
        rodadas_jogo()
    else:
        messagebox.showerror(title = 'Erro', message = 'Essa casa já está ocupada, escolha outra.')

    return rodada

def jogadaCasa6(e):
    global c6
    global rodada

    if c6 == '':
        if e == 'X':
            c6 = 'X'
            casa6Label.config(text = c6)
            casa6Label.config(fg = cor2)
            rodada = 1
        else:
            c6 = 'O'
            casa6Label.config(text = c6)
            casa6Label.config(fg = cor3)
            rodada = 2
        verifica_ganhador()
        rodadas_jogo()
    else:
        messagebox.showerror(title = 'Erro', message = 'Essa casa já está ocupada, escolha outra.')

    return rodada

def jogadaCasa7(e):
    global c7
    global rodada

    if c7 == '':
        if e == 'X':
            c7 = 'X'
            casa7Label.config(text = c7)
            casa7Label.config(fg = cor2)
            rodada = 1
        else:
            c7 = 'O'
            casa7Label.config(text = c7)
            casa7Label.config(fg = cor3)
            rodada = 2
        verifica_ganhador()
        rodadas_jogo()
    else:
        messagebox.showerror(title = 'Erro', message = 'Essa casa já está ocupada, escolha outra.')

    return rodada

def jogadaCasa8(e):
    global c8
    global rodada

    if c8 == '':
        if e == 'X':
            c8 = 'X'
            casa8Label.config(text = c8)
            casa8Label.config(fg = cor2)
            rodada = 1
        else:
            c8 = 'O'
            casa8Label.config(text = c8)
            casa8Label.config(fg = cor3)
            rodada = 2
        verifica_ganhador()
        rodadas_jogo()
    else:
        messagebox.showerror(title = 'Erro', message = 'Essa casa já está ocupada, escolha outra.')

    return rodada

def jogadaCasa9(e):
    global c9
    global rodada

    if c9 == '':
        if e == 'X':
            c9 = 'X'
            casa9Label.config(text = c9)
            casa9Label.config(fg = cor2)
            rodada = 1
        else:
            c9 = 'O'
            casa9Label.config(text = c9)
            casa9Label.config(fg = cor3)
            rodada = 2
        verifica_ganhador()
        rodadas_jogo()
    else:
        messagebox.showerror(title = 'Erro', message = 'Essa casa já está ocupada, escolha outra.')

    return rodada


#Função para o jogador 1 começar
def vezjogador1():

    btn_x1.config(state = NORMAL)
    btn_x2.config(state = NORMAL)
    btn_x3.config(state = NORMAL)
    btn_x4.config(state = NORMAL)
    btn_x5.config(state = NORMAL)
    btn_x6.config(state = NORMAL)
    btn_x7.config(state = NORMAL)
    btn_x8.config(state = NORMAL)
    btn_x9.config(state = NORMAL)

    btn_o1.config(state = DISABLED)
    btn_o2.config(state = DISABLED)
    btn_o3.config(state = DISABLED)
    btn_o4.config(state = DISABLED)
    btn_o5.config(state = DISABLED)
    btn_o6.config(state = DISABLED)
    btn_o7.config(state = DISABLED)
    btn_o8.config(state = DISABLED)
    btn_o9.config(state = DISABLED)

    btn_escolha1.config(state = DISABLED)
    btn_escolha2.config(state = DISABLED)


#Função para o jogador 2 começar
def vezjogador2():

    btn_o1.config(state = NORMAL)
    btn_o2.config(state = NORMAL)
    btn_o3.config(state = NORMAL)
    btn_o4.config(state = NORMAL)
    btn_o5.config(state = NORMAL)
    btn_o6.config(state = NORMAL)
    btn_o7.config(state = NORMAL)
    btn_o8.config(state = NORMAL)
    btn_o9.config(state = NORMAL)

    btn_x1.config(state = DISABLED)
    btn_x2.config(state = DISABLED)
    btn_x3.config(state = DISABLED)
    btn_x4.config(state = DISABLED)
    btn_x5.config(state = DISABLED)
    btn_x6.config(state = DISABLED)
    btn_x7.config(state = DISABLED)
    btn_x8.config(state = DISABLED)
    btn_x9.config(state = DISABLED)

    btn_escolha1.config(state = DISABLED)
    btn_escolha2.config(state = DISABLED)


#Função para começar o jogo Jogador vs Jogador
def comecar_jogo():
    ir_jogo()


#Frame do jogo
frame_Jogo = Frame(janela, width = 700, height = 640, bg = cor4)
frame_Jogo.place(x = 0, y = 0)

#Frame do menu
frame_Menu = Frame(janela, width = 700, height = 640, bg = cor4)
frame_Menu.place(x = 0, y = 0)

#Frame do título
frame_titulo = Frame(janela, width = 700, height = 70, bg = cor4)
frame_titulo.place(x = 0, y = 0)

frame_escolha = Frame(frame_Jogo, width = 150, height = 100, bg = cor1)
frame_escolha.place(x = 540, y = 80)

frame_voltarMenu = Frame(frame_Jogo, width = 150, height = 100, bg = cor1)
frame_voltarMenu.place(x = 10, y = 80)

frame_jogador1 = Frame(frame_Jogo, width = 300, height = 230, bg = cor2)
frame_jogador1.place(x = 0, y = 410)

frame_jogador2 = Frame(frame_Jogo, width = 300, height = 230, bg = cor3)
frame_jogador2.place(x = 400, y = 410)

#Criando Título
textotitulo = 'JOGO DA VELHA'
tituloLabel = Label(frame_titulo, text = textotitulo, width = 40, height = 2, padx = 7, bg = cor4, fg = cor1, relief = FLAT, justify = CENTER, font = ('Tahoma 20 bold'))
tituloLabel.place(x = 0, y = 0)


#Criando os botões do menu
modoLabel = Label(frame_Menu, text = 'ESCOLHA O MODO DE JOGO', width = 30, height = 2, bg = cor4, fg = cor1, justify = CENTER, font = ('Tahoma 15 bold'))
modoLabel.place(x = 150, y = 150)

btnJogador = Button(frame_Menu, command = comecar_jogo, text = 'JOGADOR VS JOGADOR', width = 25, height = 2, bg = cor1, fg = cor6, font = ('Tahoma 10 bold'))
btnJogador.place(x = 240, y = 260)

btnComputador = Button(frame_Menu, command = 0, text = 'JOGADOR VS COMPUTADOR', width = 25, height = 2, bg = cor1, fg = cor6, font = ('Tahoma 10 bold'))
btnComputador.place(x = 240, y = 330)
btnComputador.config(state = DISABLED)

breveLabel = Label(frame_Menu, text = 'EM BREVE', width = 10, height = 1, bg = cor2, fg = cor1, justify = CENTER, font = ('Tahoma 7 bold'))
breveLabel.place(x = 400, y = 325)


#Criando botão para voltar para o menu
voltarLabel = Label(frame_voltarMenu, text = 'Quer voltar \npara o menu?', width = 18, height = 2, bg = cor1, fg = cor4, padx = 1, justify = CENTER, font = ('Tahoma 10 bold'))
voltarLabel.place(x = 0, y = 5)

btn_voltar = Button(frame_voltarMenu, command = reiniciairtudo, text = 'VOLTAR', width = 10, height = 1, bg = cor4, fg = cor5, font = ('Tahoma 10 bold'))
btn_voltar.place(x = 29, y = 50)


#Criando botões de escolha de quem começa
escolhaLabel = Label(frame_escolha, text = 'Quem vai começar?', width = 18, height = 1, bg = cor1, fg = cor4, padx = 1, justify = CENTER, font = ('Tahoma 10 bold'))
escolhaLabel.place(x = 0, y = 0)

btn_escolha1 = Button(frame_escolha, command = vezjogador1, text = 'JOGADOR 1', width = 10, height = 1, bg = cor2, fg = cor5, font = ('Tahoma 10 bold'))
btn_escolha1.place(x = 29, y = 25)

btn_escolha2 = Button(frame_escolha, command = vezjogador2, text = 'JOGADOR 2', width = 10, height = 1, bg = cor3, fg = cor5, font = ('Tahoma 10 bold'))
btn_escolha2.place(x = 29, y = 60)


#Criando o Tabuleiro do jogo
#Linhas verticais
linha1 = Canvas(frame_Jogo, width = 3, height = 280)
linha1.place(x = 290, y = 100)

linha2 = Canvas(frame_Jogo, width = 3, height = 280)
linha2.place(x = 400, y = 100)

#Linhas horizontais
linha3 = Canvas(frame_Jogo, width = 280, height = 3)
linha3.place(x = 210, y = 185)

linha4 = Canvas(frame_Jogo, width = 280, height = 3)
linha4.place(x = 210, y = 285)


#Criando casas do tabuleiro
#Casas da primeira linha
casa1Label = Label(frame_Jogo, text = c1, width = 4, height = 2, bg = cor4, fg = cor1, relief = FLAT, justify = CENTER, font = ('Tahoma 20 bold'))
casa1Label.place(x = 209, y = 107)

casa2Label = Label(frame_Jogo, text = c2, width = 4, height = 2, bg = cor4, fg = cor1, relief = FLAT, justify = CENTER, font = ('Tahoma 20 bold'))
casa2Label.place(x = 310, y = 107)

casa3Label = Label(frame_Jogo, text = c3, width = 4, height = 2, bg = cor4, fg = cor1, relief = FLAT, justify = CENTER, font = ('Tahoma 20 bold'))
casa3Label.place(x = 415, y = 107)

#Casas da segunda linha
casa4Label = Label(frame_Jogo, text = c4, width = 4, height = 2, bg = cor4, fg = cor1, relief = FLAT, justify = CENTER, font = ('Tahoma 20 bold'))
casa4Label.place(x = 209, y = 202)

casa5Label = Label(frame_Jogo, text = c5, width = 4, height = 2, bg = cor4, fg = cor1, relief = FLAT, justify = CENTER, font = ('Tahoma 20 bold'))
casa5Label.place(x = 310, y = 202)

casa6Label = Label(frame_Jogo, text = c6, width = 4, height = 2, bg = cor4, fg = cor1, relief = FLAT, justify = CENTER, font = ('Tahoma 20 bold'))
casa6Label.place(x = 415, y = 202)

#Casas da terceira linha
casa7Label = Label(frame_Jogo, text = c7, width = 4, height = 2, bg = cor4, fg = cor1, relief = FLAT, justify = CENTER, font = ('Tahoma 20 bold'))
casa7Label.place(x = 209, y = 300)

casa8Label = Label(frame_Jogo, text = c8, width = 4, height = 2, bg = cor4, fg = cor1, relief = FLAT, justify = CENTER, font = ('Tahoma 20 bold'))
casa8Label.place(x = 310, y = 300)

casa9Label = Label(frame_Jogo, text = c9, width = 4, height = 2, bg = cor4, fg = cor1, relief = FLAT, justify = CENTER, font = ('Tahoma 20 bold'))
casa9Label.place(x = 415, y = 300)


#Criando Titulos dos jogadores
textojogador1 = 'JOGADOR 1'
jogador1Label = Label(frame_jogador1, text = textojogador1, width = 33, height = 1, bg = cor2, fg = cor1, relief = FLAT, justify = CENTER, font = ('Tahoma 11 bold'))
jogador1Label.place(x = 0, y = 5)

textojogador2 = 'JOGADOR 2'
jogador2Label = Label(frame_jogador2, text = textojogador2, width = 33, height = 1, bg = cor3, fg = cor1, relief = FLAT, justify = CENTER, font = ('Tahoma 11 bold'))
jogador2Label.place(x = 0, y = 5)


#Criando os botões do JOGADOR 1
#Botões da primeira linha
btn_x1 = Button(frame_jogador1, command = lambda: jogadaCasa1('X'), text = 'X', width = 4, height= 2, bg = cor4, fg = cor1, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_x1.place(x = 65, y = 40)
btn_x1.config(state = DISABLED)

btn_x2 = Button(frame_jogador1, command = lambda: jogadaCasa2('X'), text = 'X', width = 4, height= 2, bg = cor4, fg = cor1, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_x2.place(x = 125, y = 40)
btn_x2.config(state = DISABLED)

btn_x3 = Button(frame_jogador1, command = lambda: jogadaCasa3('X'), text = 'X', width = 4, height= 2, bg = cor4, fg = cor1, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_x3.place(x = 185, y = 40)
btn_x3.config(state = DISABLED)

#Botões da segunda linha
btn_x4 = Button(frame_jogador1, command = lambda: jogadaCasa4('X'), text = 'X', width = 4, height= 2, bg = cor4, fg = cor1, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_x4.place(x = 65, y = 100)
btn_x4.config(state = DISABLED)

btn_x5 = Button(frame_jogador1, command = lambda: jogadaCasa5('X'), text = 'X', width = 4, height= 2, bg = cor4, fg = cor1, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_x5.place(x = 125, y = 100)
btn_x5.config(state = DISABLED)

btn_x6 = Button(frame_jogador1, command = lambda: jogadaCasa6('X'), text = 'X', width = 4, height= 2, bg = cor4, fg = cor1, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_x6.place(x = 185, y = 100)
btn_x6.config(state = DISABLED)

#Botões da terceira linha
btn_x7 = Button(frame_jogador1, command = lambda: jogadaCasa7('X'), text = 'X', width = 4, height= 2, bg = cor4, fg = cor1, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_x7.place(x = 65, y = 160)
btn_x7.config(state = DISABLED)

btn_x8 = Button(frame_jogador1, command = lambda: jogadaCasa8('X'), text = 'X', width = 4, height= 2, bg = cor4, fg = cor1, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_x8.place(x = 125, y = 160)
btn_x8.config(state = DISABLED)

btn_x9 = Button(frame_jogador1, command = lambda: jogadaCasa9('X'), text = 'X', width = 4, height= 2, bg = cor4, fg = cor1, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_x9.place(x = 185, y = 160)
btn_x9.config(state = DISABLED)


#Criando os botões do JOGADOR 2
#Botões da primeira linha
btn_o1 = Button(frame_jogador2, command = lambda: jogadaCasa1('O'), text = 'O', width = 4, height= 2, bg = cor4, fg = cor1, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_o1.place(x = 65, y = 40)
btn_o1.config(state = DISABLED)

btn_o2 = Button(frame_jogador2, command = lambda: jogadaCasa2('O'), text = 'O', width = 4, height= 2, bg = cor4, fg = cor1, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_o2.place(x = 125, y = 40)
btn_o2.config(state = DISABLED)

btn_o3 = Button(frame_jogador2, command = lambda: jogadaCasa3('O'), text = 'O', width = 4, height= 2, bg = cor4, fg = cor1, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_o3.place(x = 185, y = 40)
btn_o3.config(state = DISABLED)

#Botões da segunda linha
btn_o4 = Button(frame_jogador2, command = lambda: jogadaCasa4('O'), text = 'O', width = 4, height= 2, bg = cor4, fg = cor1, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_o4.place(x = 65, y = 100)
btn_o4.config(state = DISABLED)

btn_o5 = Button(frame_jogador2, command = lambda: jogadaCasa5('O'), text = 'O', width = 4, height= 2, bg = cor4, fg = cor1, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_o5.place(x = 125, y = 100)
btn_o5.config(state = DISABLED)

btn_o6 = Button(frame_jogador2, command = lambda: jogadaCasa6('O'), text = 'O', width = 4, height= 2, bg = cor4, fg = cor1, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_o6.place(x = 185, y = 100)
btn_o6.config(state = DISABLED)

#Botões da terceira linha
btn_o7 = Button(frame_jogador2, command = lambda: jogadaCasa7('O'), text = 'O', width = 4, height= 2, bg = cor4, fg = cor1, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_o7.place(x = 65, y = 160)
btn_o7.config(state = DISABLED)

btn_o8 = Button(frame_jogador2, command = lambda: jogadaCasa8('O'), text = 'O', width = 4, height= 2, bg = cor4, fg = cor1, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_o8.place(x = 125, y = 160)
btn_o8.config(state = DISABLED)

btn_o9 = Button(frame_jogador2, command = lambda: jogadaCasa9('O'), text = 'O', width = 4, height= 2, bg = cor4, fg = cor1, font = ('Tahoma 12 bold'), relief = RAISED, overrelief = RIDGE)
btn_o9.place(x = 185, y = 160)
btn_o9.config(state = DISABLED)



frame_Menu.pack()
janela.mainloop()