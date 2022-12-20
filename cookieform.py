

import tkinter as tk
from tkinter import ttk
from tkinter import Button, Entry, Label,Tk
from tkinter.messagebox import showinfo


class CookieOrderForm(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('Cookie Form')
        self.geometry("250x150")

        # label
        self.label1 = ttk.Label(self, text='Choco Chips($1.00):').grid(row=0)
        self.label2 = ttk.Label(self, text='     Oat Meal($1.50):').grid(row=1)
        self.label3 = ttk.Label(self, text='         Oreyo ($2.00):').grid(row=2)
        self.e1 = ttk.Entry(self)
        self.e2 = ttk.Entry(self)
        self.e3 = ttk.Entry(self)
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)
        # button
        self.button = ttk.Button(self, text='Order Total',command=self.Total).grid(row=3,column=1)
        
        
        

    def Total(self):
            self.g1 = self.e1.get()
            self.g2 = self.e2.get()
            self.g3 = self.e3.get()
            self.Make_widgets()
            
    def Make_widgets(self):
            x=self.g1
            y=self.g2
            z=self.g3
            xn=x.isnumeric()
            yn=y.isnumeric()
            zn=z.isnumeric()
            
            if xn==False:
                    showinfo("Cookie Count","Error!:Incorrect Value Entered in Choco Chips!")
            elif yn==False:
                    showinfo("Cookie Count","Error!:Incorrect Value Entered in Oatmeals!")
            elif zn==False:
                    showinfo("Cookie Count","Error!:Incorrect Value Entered in Oreyo!")
            if xn==True and yn==True and zn==True:
                    xx=int(self.g1)
                    yy=float(self.g2)
                    zz=int(self.g3)
                    to=xx*1+yy*1.5+zz*2
                    showinfo("Total","Your order total is ${0}".format(to)) 
           


if __name__ == "__main__":
    cookieOrderForm = CookieOrderForm()
    cookieOrderForm.mainloop()