import tkinter as tk
from tkinter import messagebox
import requests as r
import constants
api=constants.api_key
class App:
    def __init__(self, master):
        self.master=master
        self.master.geometry("600x400")
        self.varos=tk.StringVar()
        self.varos_label=tk.Label(master, text="Város")
        self.varos_input=tk.Entry(master, textvariable=self.varos)
        self.varos_label.grid(row=0, column=0)
        self.varos_label.grid_anchor(anchor="center")
        self.varos_input.grid(row=0, column=1)
        self.varos_input.grid_anchor(anchor="center")
        self.gomb=tk.Button(master, text="Submit", command=self.temp_c)
        self.gomb.grid(row=2, column=1)
        self.gomb.grid_anchor(anchor="center")
    def temp_c(self):
        varos_ertek=self.varos.get()
        site=r.get(f"http://api.weatherapi.com/v1/current.json?key={api}&q={varos_ertek}&aqi=no")
        if site.status_code!=200:
            messagebox.showinfo("Hiba", "Helytelen város.")
        else:
            data=site.json()['current']
            messagebox.showinfo("Temperature", f"{varos_ertek}: {data['temp_c']}C°")
        
        
ablak=tk.Tk()
app=App(ablak)
ablak.mainloop()