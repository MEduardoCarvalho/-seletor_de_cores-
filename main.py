from tkinter import *
import tkinter.messagebox

#cores
cor0 = "#444466"  # Preta
cor1 = "#feffff"  # branca
cor2 = "#004338"  

#criando a janela
janela = Tk()
janela.geometry("530x205")
janela.configure(bg=cor1)

#configuraçao da janela 
tela = Label(janela, bg=cor0, width=40, height=10,  bd=1)
tela.grid(row=0 , column=0)

frame_direito = Frame(janela, bg=cor1)
frame_direito.grid(row=0 , column=1, padx=5) 

frame_baixo = Frame(janela , bg=cor1)
frame_baixo.grid(row=1 , column=0, columnspan=2, pady=15)

#Funçao scale
def escala(valor):
    r=s_red.get()
    g=s_green.get()
    b=s_blue.get()

    rgb = f"{r} , {g} , {b}"

    hexaDecimal= "#%02x%02x%02x" % (r,g,b)

    #altera a cor do fundo da tela
    tela["bg"] = hexaDecimal

    #altera o entry
    e_cor.delete(0,END)
    e_cor.insert(0,hexaDecimal)

#funçao clicar
def onClick():
    #informar
    tkinter.messagebox.showinfo("cor", "a cor foi copiada")
    #criar botao copiar
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(e_cor.get())
    clip.destroy()

#configuraçao do frame direito 
#red
l_red = Label(frame_direito,text="Red", width=7 , bg=cor1 , fg="red" , anchor="nw", font=("time new roman", 12 , "bold"))
l_red.grid(row=0 , column=0)
s_red=Scale(frame_direito,command=escala, from_=0 , to=255 ,length=150, bg=cor1, fg="red", orient=HORIZONTAL)
s_red.grid(row=0, column=1)
#green
l_green = Label(frame_direito,text="Green", width=7 , bg=cor1 , fg="green" , anchor="nw", font=("time new roman", 12 , "bold"))
l_green.grid(row=1 , column=0)
s_green=Scale(frame_direito, command=escala,from_=0 , to=255 ,length=150, bg=cor1, fg="green", orient=HORIZONTAL)
s_green.grid(row=1, column=1)
#blue
l_blue = Label(frame_direito,text="Blue", width=7 , bg=cor1 , fg="blue" , anchor="nw", font=("time new roman", 12 , "bold"))
l_blue.grid(row=2, column=0)
s_blue=Scale(frame_direito, command=escala,from_=0 , to=255 ,length=150, bg=cor1, fg="blue", orient=HORIZONTAL)
s_blue.grid(row=2, column=1)

#configuraçao do frame baixo
l_rgb = Label(frame_baixo,text="CÓDIGO HEX:", bg=cor1 , font=("Ivy", 10 , "bold"))
l_rgb.grid(row=0 , column=0,padx=5)

#entry
e_cor = Entry(frame_baixo, width=12 , font=("Ivy", 10 , "bold"), justify=CENTER)
e_cor.grid(row=0 , column=1,padx=5)

#botao copiar
b_copiar = Button(frame_baixo,command = onClick,text="copiar a cor", bg=cor1 , font=("Ivy", 8 , "bold"), relief=RAISED, overrelief=RIDGE)
b_copiar.grid(row=0 , column=2,padx=5)

#app name 
l_app_nome = Label(frame_baixo,text="Seletor de Cores", bg=cor1 , font=("Ivy", 15 , "bold"))
l_app_nome.grid(row=0 , column=3,padx=40)

#janela funcionando
janela.mainloop()