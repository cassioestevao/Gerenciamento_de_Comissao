import customtkinter
from tkinter import *

customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('green')

root = customtkinter.CTk()
root.geometry('1024x512')
root.title('Dev | Desenvolvimento de Aplicativo de Gerenciamento de Estoque')
root.iconbitmap('icon.ico')
root.resizable(False,False)

color_login = '#F97D7D'

# IMAGEM
img = PhotoImage(file='img.png')
label_img = customtkinter.CTkLabel(master=root, image=img)
label_img.place(x=5, y=40)
label_img.configure(text='')

# FRAME
frame = customtkinter.CTkFrame(master=root, width=512, height=510)
frame.pack(side=RIGHT)

# FRAMEWIDGET
label = customtkinter.CTkLabel(master=frame,text='Gerenciamento de Estoque',font=('Century Gothic',30),text_color=color_login)
label.place(x=60,y=30)

entry_nome = customtkinter.CTkEntry(master=frame, placeholder_text='Digite o seu usuário', width=300, font=('Century Gothic',15),corner_radius=20,fg_color=color_login,text_color='black',placeholder_text_color='white',border_color=color_login,border_width=0)
entry_nome.place(x=125, y=186)

label_inf_user = customtkinter.CTkLabel(master=frame, text='*O campo de usuário é de carater obrigatorio.',font=('Century Gothic',12),text_color='black')
label_inf_user.place(x=125, y=216)

entry_senha = customtkinter.CTkEntry(master=frame, placeholder_text='Digite a sua senha',width=300,font=('Century Gothic',15),corner_radius=20,fg_color=color_login,text_color='black',placeholder_text_color='white',border_color=color_login,border_width=0)
entry_senha.place(x=125, y=246)

label_inf_pass =customtkinter.CTkLabel(master=frame, text='*O compo de senha é de carater obrigatorio.',font=('Century Gothic',12),text_color='black')
label_inf_pass.place(x=125,y=276)

#-------------------------------------------------------------------------

#check box
checkbox = customtkinter.CTkCheckBox(master=frame, text='Lembrar de mim ?', fg_color=color_login,border_color='white')
checkbox.place(x=125, y=316)


button_login = customtkinter.CTkButton(master=frame, text='Login',font=('Century Gothic',15),corner_radius=10,fg_color=color_login)
button_login.place(x=125, y=366)

button_login_regis = customtkinter.CTkButton(master=frame, text='Registrar',font=('Century Gothic',15),corner_radius=10,fg_color=color_login)
button_login_regis.place(x=280, y=366)



root.mainloop()