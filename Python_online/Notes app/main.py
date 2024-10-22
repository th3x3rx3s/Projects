import tkinter as tk
from tkinter import messagebox
import os
class App:
    def __init__(self, master):
        self.master=master
        master.geometry("750x500")
        master.title("Szövegszerkesztő")
        #MENÜSÁV
        self.menusav=tk.Menu(master)
        self.optmenu=tk.Menu(self.menusav, tearoff=0)
        self.optmenu.add_command(label="Mentés másként...", command=self.save_as)
        self.menusav.add_cascade(label="Opciók", menu=self.optmenu)
        master.configure(menu=self.menusav)

        #SZÖVEG DOBOZ
        self.text=tk.Text(master, height=master.winfo_screenheight(), width=master.winfo_screenwidth())
        self.text.pack()
        self.text.configure(font=("Helvetica", 11, "normal"))
    def save_as(self):
        self.szoveg=self.text.get(1.0, tk.END)
        self.popup_ablak=tk.Toplevel()
        self.popup_ablak.geometry("500x300")
        self.popup_ablak.title("Mentés másként...")
        self.name=tk.StringVar()
        self.name_label=tk.Label(self.popup_ablak, text="Mi legyen a neve?")
        self.name_entry=tk.Entry(self.popup_ablak, textvariable=self.name)
        self.name_label.grid(row=0,column=0)
        self.name_entry.grid(row=0,column=1)
        self.gomb=tk.Button(self.popup_ablak, text="Ok", command=self.save_text)
        self.gomb.grid(row=2,column=1)
    def save_text(self):
        nev=self.name.get()
        path=os.path.join(os.path.dirname(os.path.realpath(__file__)), nev)
        with open(path, "w") as f:
            f.write(self.szoveg)
        self.popup_ablak.destroy()
ablak=tk.Tk()
app=App(ablak)
ablak.mainloop()