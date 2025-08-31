import tkinter as tk
from PIL import Image,ImageTk
from tkinter import PhotoImage
from pathlib import Path

JOHNPORK=Path(__file__).resolve().parent / "Prok.png"

janela=tk.Tk()

janela.title("Pork Alert")
janela.geometry("350x250")

txtpork=tk.Label(janela,text="PORK ALERT",fg="red",font="Calibri")
txtpork.pack(pady=10)

pork_image=Image.open(JOHNPORK)
pork_image=pork_image.resize((100,100))
john_image=ImageTk.PhotoImage(pork_image)

label_pork=tk.Label(janela,image=john_image)
label_pork.pack(pady=10)

btnok=tk.Button(janela,text="OK",command=janela.destroy)
btnok.pack(pady=10)

janela.mainloop() #O que você procura aqui?