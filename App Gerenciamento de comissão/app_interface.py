import customtkinter as ctk
from PIL import Image, ImageTk

color_login = '#F97D7D'

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

MenuPrincipal = ctk.CTk()
MenuPrincipal.title('Banco de dados | DEV Cássio Estevão')
MenuPrincipal.iconbitmap('icon.ico')
MenuPrincipal.geometry('800x500')
MenuPrincipal.resizable(False, False)

largura_desejada = 500
altura_desejada = 400

# Desenvolvendo interface
# Título do Menu principal
text_label_title = ctk.CTkLabel(master=MenuPrincipal, text='Gerenciamento de comissão', font=('Century Gothic', 30), text_color=color_login)
text_label_title.place(x=180, y=5)

# Botões
btn_calculo = ctk.CTkButton(master=MenuPrincipal, text='Calculo', font=('Century Gothic', 15), fg_color=color_login)
btn_calculo.place(x=40, y=70)
btn_faturamento = ctk.CTkButton(master=MenuPrincipal, text='Faturamento', font=('Century Gothic', 15))
btn_faturamento.place(x=190, y=70)
btn_graficos = ctk.CTkButton(master=MenuPrincipal, text='Graficos', font=('Century Gothic', 15), fg_color=color_login)
btn_graficos.place(x=340, y=70)
btn_dados = ctk.CTkButton(master=MenuPrincipal, text='Dados', font=('Century Gothic', 15), fg_color=color_login)
btn_dados.place(x=490, y=70)

# Frame de exibição
frm_exibe = ctk.CTkFrame(master=MenuPrincipal, width=590, height=356, fg_color='transparent')
frm_exibe.place(x=40, y=120)

image = Image.open('login.png')
image = image.resize((largura_desejada, altura_desejada))
img = ImageTk.PhotoImage(image)

label_img = ctk.CTkLabel(master=frm_exibe, image=img)
label_img.configure(text='')
label_img.pack(padx=40, pady=1)

# Botões de exportação
btn_abrir = ctk.CTkButton(master=MenuPrincipal, text='ABRIR',corner_radius=15,border_color=None ,font=('Century Gothic', 15), fg_color=color_login)
btn_abrir.place(x=646, y=150)
btn_import = ctk.CTkButton(master=MenuPrincipal, text='IMPORTAR',corner_radius=15,border_color=None ,font=('Century Gothic', 15), fg_color=color_login,)
btn_import.place(x=646, y=190)
btn_export = ctk.CTkButton(master=MenuPrincipal, text='EXPORTAR',corner_radius=15,border_color=None ,font=('Century Gothic', 15), fg_color=color_login)
btn_export.place(x=646, y=230)

MenuPrincipal.mainloop()
