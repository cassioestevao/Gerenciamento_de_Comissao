import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageOps, ImageChops
from tkinter import PhotoImage


ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

def remove_background():
    file_path = filedialog.askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg")])
    if not file_path:
        return
    img = Image.open(file_path).convert("RGBA")
    bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
    img_without_bg = Image.alpha_composite(bg, img)
    img_without_bg = img_without_bg.convert("RGB")

    save_path = filedialog.asksaveasfilename(defaultextension='.jpg', filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")])
    if not save_path:
        return
    img_without_bg.save(save_path)

root = ctk.CTk()
root.title("Dev (cassioestevao) | Converso de imagem")
root.geometry('400x500')
root.iconbitmap('iconAPI.ico')
root.resizable(False,False)     

text_label = ctk.CTkLabel(master=root, text='Desenvolvido por\n Dev | Cássio Estevão (cassioestevao)',font=('Century Gothic',17))
text_label.pack(padx=10,pady=40)

#Photo logan


#logo_path = 'C:\Users\Windows\Desktop\Gerenciamento\img\logo.png'  # Substitua pelo caminho correto da sua logo
#logo_img = Image.open(logo_path)
#logo_tk = ImageTk.PhotoImage(logo_img)
# OBSSSSS !!!


#logo_label = tk.Label(root, image=logo_tk)
#logo_label.image = logo_tk  # Manter uma referência
#logo_label.place(x=10, y=10)

btn = ctk.CTkButton(root, text="Selecionar Imagem",font=('Century Gothic',18), command=remove_background,corner_radius=18,border_color=None,fg_color='yellow',text_color='black',hover_color='blue')
btn.pack(padx=20, pady=160)

root.mainloop()
