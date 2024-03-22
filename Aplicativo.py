import customtkinter as ctk
from tkinter import *
import database
from tkinter import messagebox

root = ctk.CTk()
color_login = '#F97D7D'

class App_gerenciamento():
    def __init__(self):
        self.root = root
        self.Theme()
        self.Paramentros_de_Tela()
        self.Menu_login()
        root.mainloop()
        
    def Theme(self):
        ctk.set_appearance_mode('light')
        ctk.set_default_color_theme('green')

    def Paramentros_de_Tela(self):
        root.geometry('1024x512')
        root.title('Dev Cássio Estevão (cassioestevao) | Desenvolvimento de Aplicativo de Gerenciamento de comissão')
        root.iconbitmap('icon.ico')
        root.resizable(False,False)

    def Menu_login(self):
        img = PhotoImage(file='img.png')
        label_img = ctk.CTkLabel(master=root, image=img)
        label_img.place(x=5, y=40)
        label_img.configure(text='')

        # FRAME
        frame_login = ctk.CTkFrame(master=root, width=512, height=510)
        frame_login.pack(side=RIGHT)

        # FRAME WIDGET
        label_title = ctk.CTkLabel(master=frame_login,text='Gerenciamento de comissão',font=('Century Gothic',30),text_color=color_login).place(x=50,y=80)
        entry_nome = ctk.CTkEntry(master=frame_login, placeholder_text='Digite o seu usuário', width=300, font=('Century Gothic',15),corner_radius=20,fg_color=color_login,text_color='black',placeholder_text_color='white',border_color=color_login,border_width=0).place(x=125, y=186)
        label_inf_user = ctk.CTkLabel(master=frame_login, text='*O campo de usuário é de carater obrigatorio.',font=('Century Gothic',12),text_color='black').place(x=125, y=216)
        entry_senha = ctk.CTkEntry(master=frame_login, placeholder_text='Digite a sua senha',width=300,font=('Century Gothic',15),corner_radius=20,fg_color=color_login,text_color='black',placeholder_text_color='white',border_color=color_login,border_width=0,show='*').place(x=125, y=246)
        label_inf_pass =ctk.CTkLabel(master=frame_login, text='*O compo de senha é de carater obrigatorio.',font=('Century Gothic',12),text_color='black').place(x=125,y=276)
    
        #check box
        checkbox = ctk.CTkCheckBox(master=frame_login, text='Lembrar de mim ?', fg_color=color_login,border_color=color_login,hover_color=color_login,corner_radius=20,font=('Century Gothic',12)).place(x=125, y=316)
        def login():
           
            msg = messagebox.showerror(message='Usuario, não encotrado!',title='Atenção!')
    
        button_login = ctk.CTkButton(master=frame_login, text='Login',font=('Century Gothic',15),corner_radius=10,fg_color=color_login,command=login).place(x=125, y=366)
        
        def Cadastro_menu():
            #remover frame de login
            frame_login.pack_forget()
            
            #frame registro
            frame_registro = ctk.CTkFrame(master=root, width=512, height=510)
            frame_registro.pack(side=RIGHT)
            
            
            label_title_registro = ctk.CTkLabel(master=frame_registro,text='Cadastro de Usuário',font=('Century Gothic',30),text_color=color_login).place(x=120,y=70)
            span = ctk.CTkLabel(master=frame_registro,text='*Preencha todos os dados corretamente!', font=('Century Gothic',12)).place(x=140,y=130)

            entry_menu_registro_user = ctk.CTkEntry(master=frame_registro, placeholder_text='Digite um nome de usuário', width=300, font=('Century Gothic',15),corner_radius=20,fg_color=color_login,text_color='black',placeholder_text_color='white',border_color=color_login,border_width=0).place(x=125, y=186)
            entry_menu_registro_email = ctk.CTkEntry(master=frame_registro, placeholder_text='Digite seu e-mail', width=300, font=('Century Gothic',15),corner_radius=20,fg_color=color_login,text_color='black',placeholder_text_color='white',border_color=color_login,border_width=0).place(x=125, y=226)

            entry_menu_registro_password = ctk.CTkEntry(master=frame_registro, placeholder_text='Digite a sua senha', width=300, font=('Century Gothic',15),corner_radius=20,fg_color=color_login,text_color='black',placeholder_text_color='white',border_color=color_login,border_width=0,show='*').place(x=125, y=266)
            entry_menu_registro_conf_password = ctk.CTkEntry(master=frame_registro, placeholder_text='Confirme a sua senha', width=300, font=('Century Gothic',15),corner_radius=20,fg_color=color_login,text_color='black',placeholder_text_color='white',border_color=color_login,border_width=0,show='*').place(x=125, y=306)
            termos_user =ctk.CTkCheckBox(master=frame_registro, text='*Aceito todos os Termos e Politicas',fg_color='green',border_color='green',corner_radius=20,font=('Century Gothic',12)).place(x=125,y=346)
            
            def back_regist(): 
                #remover o frame de registro
                frame_registro.forget()
                # chamando o frame de registro
                frame_login.pack(side=RIGHT)
                
            button_menu_back = ctk.CTkButton(master=frame_registro,text='Voltar',fg_color=color_login,font=('Century Gothic',15),corner_radius=10,command=back_regist).place(x=125,y=400)
            def save_registro():
                msg = messagebox.showinfo(message='Registro concluído, por favor verifique o seu e-mail.', title="Notificação de Cadastro!")
                pass
            button_save_registro = ctk.CTkButton(master=frame_registro,text='Concluir',fg_color='green',font=('Century Gothic',15),corner_radius=10,command=save_registro).place(x=290,y=400)
         
        button_login_regis = ctk.CTkButton(master=frame_login, text='Registrar',font=('Century Gothic',15),corner_radius=10,fg_color=color_login,command=Cadastro_menu).place(x=280, y=366)


App_gerenciamento() 