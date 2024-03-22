import customtkinter as ctk
import pandas 
from tkinter import*
from tkinter import PhotoImage
from PIL import Image, ImageTk

color_login = '#F97D7D'

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

MenuPrincipal = ctk.CTk()
MenuPrincipal.title('Banco de dados | DEV Cássio Estevão')
MenuPrincipal.iconbitmap('icon.ico')
MenuPrincipal.geometry('800x500')
MenuPrincipal.resizable(False,False)

largura_desejada = 590
altura_desejada = 400

#desenvolvendo interface
#Titulo do Menu principal
text_label_title = ctk.CTkLabel(master=MenuPrincipal,text='Gerenciamento de comissão',font=('Century Gothic',30),text_color=color_login).place(x=180,y=5)

#botões
btn_calculo = ctk.CTkButton(master=MenuPrincipal, text='Calculo',font=('Century Gothic',12),fg_color=color_login).place(x=40,y=70)
btn_faturamento = ctk.CTkButton(master=MenuPrincipal, text='Faturamento',font=('Century Gothic',12)).place(x=190,y=70)
btn_graficos = ctk.CTkButton(master=MenuPrincipal, text='Graficos',font=('Century Gothic',12),fg_color=color_login).place(x=340,y=70)
btn_dados = ctk.CTkButton(master=MenuPrincipal, text='Dados',font=('Century Gothic',12),fg_color=color_login).place(x=490,y=70)


#frame de exibição
frm_exibe = ctk.CTkFrame(master=MenuPrincipal, width=590, height=356,fg_color='transparent')
frm_exibe.place(x=40,y=120)

image = Image.open('login.png')
# Cria uma instância de CTkImage com a imagem
img = ImageTk.PhotoImage(image)

image = image.resize((largura_desejada, altura_desejada))
img = ImageTk.PhotoImage(image)

label_img = ctk.CTkLabel(master=frm_exibe, image=img)
label_img.configure(text='')
label_img.pack()


#botoes de exportação
btn_abrir =ctk.CTkButton(master=MenuPrincipal,text ='Abrir',font=('Century Gothic',12),fg_color=color_login).place(x=646,y=150)
btn_import =ctk.CTkButton(master=MenuPrincipal,text ='Importar',font=('Century Gothic',12),fg_color=color_login).place(x=646,y=190)


MenuPrincipal.mainloop()
