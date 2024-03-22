import customtkinter as ctk
import pandas 
from tkinter import*
from tkinter import PhotoImage


color_login = '#F97D7D'

ctk.set_appearance_mode('light')
ctk.set_default_color_theme('green')

MenuPrincipal = ctk.CTk()
MenuPrincipal.title('Banco de dados | DEV Cássio Estevão')
MenuPrincipal.iconbitmap('icon.ico')
MenuPrincipal.geometry('800x500')
MenuPrincipal.resizable(False,False)

#desenvolvendo interface
#Titulo do Menu principal
text_label_title = ctk.CTkLabel(master=MenuPrincipal,text='Gerenciamento de comissão',font=('Century Gothic',30),text_color=color_login).place(x=180,y=5)

#botões
btn_calculo = ctk.CTkButton(master=MenuPrincipal, text='Calculo',font=('Century Gothic',12),fg_color=color_login).place(x=40,y=70)
btn_faturamento = ctk.CTkButton(master=MenuPrincipal, text='Faturamento',font=('Century Gothic',12)).place(x=190,y=70)
btn_graficos = ctk.CTkButton(master=MenuPrincipal, text='Graficos',font=('Century Gothic',12),fg_color=color_login).place(x=340,y=70)
btn_dados = ctk.CTkButton(master=MenuPrincipal, text='Dados',font=('Century Gothic',12),fg_color=color_login).place(x=490,y=70)

#frame de exibição
frm_exibe = ctk.CTkFrame(master=MenuPrincipal, width=590, height=356).place(x=40,y=120)
img = PhotoImage(file='login.png')

width, height = img.width(), img.height()
new_width, new_height = 550, 425  # Defina o novo tamanho desejado

# Cria uma nova imagem com o novo tamanho
img = img.subsample(round(width/new_width), round(height/new_height))


label_img = ctk.CTkLabel(master=frm_exibe, image=img,bg_color='transparent',fg_color='transparent')
label_img.place(x=40, y=130)
label_img.configure(text='')

#botoes de exportação
btn_abrir =ctk.CTkButton(master=MenuPrincipal,text ='Abrir',font=('Century Gothic',12),fg_color=color_login).place(x=646,y=150)
btn_import =ctk.CTkButton(master=MenuPrincipal,text ='Importar',font=('Century Gothic',12),fg_color=color_login).place(x=646,y=190)


MenuPrincipal.mainloop()