import customtkinter as ctk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
from pandastable import Table
from tkintertable import TableCanvas, TableModel
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg




root = ctk.CTk()
color_login = '#F97D7D'
largura_desejada = 500
altura_desejada = 356

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
        
        
    #NOVA IMAGEM E JANELAS 
        def open_new_window():
            ctk.set_appearance_mode('light')
            ctk.set_default_color_theme('green')
            
            root.destroy()

            MenuPrincipal = ctk.CTk()
            MenuPrincipal.title('Banco de dados | DEV Cássio Estevão')
            MenuPrincipal.iconbitmap('icon.ico')
            MenuPrincipal.geometry('1024x512')
            MenuPrincipal.resizable(False, False)
            
            # Desenvolvendo interface
            # Título do Menu principal
            text_label_title = ctk.CTkLabel(master=MenuPrincipal, text='Gerenciamento de comissão', font=('Century Gothic', 30), text_color=color_login)
            text_label_title.place(x=180, y=5)
            
            label_option = ctk.CTkFrame(master=MenuPrincipal, width=685, height=43, bg_color='transparent',fg_color='transparent',border_color=color_login,border_width=2).place(x=30, y=63)
        
        # BOTÕES SUPERIOR MENU PRINCIPAL
            btn_calculo = ctk.CTkButton(master=MenuPrincipal, text='Dados',bg_color='transparent', font=('Century Gothic', 15), fg_color=color_login,corner_radius=10)
            btn_calculo.place(x=40, y=70)
            btn_faturamento = ctk.CTkButton(master=MenuPrincipal, text='Faturamento',bg_color='transparent',fg_color=color_login, font=('Century Gothic', 15),corner_radius=10)
            btn_faturamento.place(x=215, y=70)
            btn_graficos = ctk.CTkButton(master=MenuPrincipal, text='Graficos',bg_color='transparent', font=('Century Gothic', 15), fg_color=color_login,corner_radius=10)
            btn_graficos.place(x=390, y=70)
            btn_dados = ctk.CTkButton(master=MenuPrincipal, text='Calculos',bg_color='transparent', font=('Century Gothic', 15), fg_color=color_login,corner_radius=10)
            btn_dados.place(x=565, y=70)

            # Frame de exibição
            frm_exibe = ctk.CTkFrame(master=MenuPrincipal, width=665, height=350, fg_color=color_login, corner_radius=30)
            frm_exibe.place(x=40, y=120)


            # Calcular a largura das colunas com base no conteúdo das células


         # Calcular a largura das colunas com base no conteúdo das células
          # Calcular a largura das colunas com base no conteúdo das células
         #   def calculateColumnWidths(table_model):
          #      column_widths = []
          #      for col in range(table_model.getColumnCount()):
         #           max_width = max([len(str(table_model.getValueAt(row, col))) for row in range(table_model.getRowCount())])
         #           column_widths.append(max_width * 3)  # Multiplicar pelo tamanho médio de um caractere
         #       return column_widths

            

            def open_file():
                file_path = filedialog.askopenfilename(filetypes=[('Excel Files', '*.xlsx *.xls')])
                if file_path:
                    df = pd.read_excel(file_path)

        # Reorganizar as colunas para a orientação correta
                    df = df.transpose()
                    table_model = TableModel(dataframe=df)

                    table = Table(frm_exibe, model=table_model)
                    table.configure(cellbackground='white', cellforeground='black', rowselectedcolor='orange', rowheaderbackground='gray', rowheaderforeground='white', font=('Helvetica', 10), headerfont=('Helvetica', 10, 'bold'))

                    # Oculta a coluna de índices
                    table.showIndex()
                    table.redraw()

                    # Oculta a legenda do eixo y


                    table.show()

                    MenuPrincipal.update()

            # BOTÕES DE EXPORTAÇÃO
            btn_abrir = ctk.CTkButton(master=MenuPrincipal, text='Abrir',corner_radius=15,border_color=None ,font=('Century Gothic', 14), fg_color=color_login,command=open_file)
            btn_abrir.place(x=80, y=476)
            btn_import = ctk.CTkButton(master=MenuPrincipal, text='Importar',corner_radius=15,border_color=None ,font=('Century Gothic', 14), fg_color=color_login,)
            btn_import.place(x=255, y=476)
#TEMAA
            
            def mudar_tema():
                ctk.set_appearance_mode('dark')
                ctk.set_default_color_theme('dark-blue')
                color_login = mudar_tema

            btn_export = ctk.CTkButton(master=MenuPrincipal, text='Modo noturno!',corner_radius=15,border_color=None ,font=('Century Gothic', 14), fg_color=color_login,command=mudar_tema)
            btn_export.place(x=850, y=476)

            MenuPrincipal.mainloop()

 ###########################  FINALIZAÇÕES ###################################################
            
        def login():
            username = entry_nome.get()
            password = entry_senha.get()

    # Verificar as credenciais do usuário
            if username == 'admin' and password == 'admin':
                root.destroy()  # Fecha a janela de login
                open_new_window()
            else:
                messagebox.showerror("Erro de login", "Credenciais inválidas")

 ##########################################################################################               

        button_login = ctk.CTkButton(master=frame_login, text='Login',font=('Century Gothic',15),corner_radius=10,fg_color=color_login,command=open_new_window).place(x=125, y=366)
        
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
