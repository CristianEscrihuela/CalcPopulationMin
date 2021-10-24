"""
Copyright 2021 Cristian Escrihuela Benages

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

"""

#! /usr/bin/env python3

from tkinter import Menu, PhotoImage, Tk, DoubleVar, IntVar, Toplevel, messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk
from decimal import *
import math
import sys
import os


class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.p = DoubleVar()
        self.prob_error_P = DoubleVar()
        self.k = IntVar()
        self.r = IntVar()

        self.style = ttk.Style()
        self.style.configure("R.TLabel", foreground="black", background="#56FFC7", borderwidth=5, anchor="e", font=('Helvetica', 18, 'bold'))
        self.style.configure("Res.TLabel", font=('Helvetica', 10, 'bold'))
        self.style.configure("Normal.TLabel", font=('Helvetica', 10))
        self.style.configure("Button.TButton", font=("Helvetica", 12, 'bold'), padding="0 10 0 10")
 
        self.label1_p = ttk.Label(self, style="Normal.TLabel", text="Probabilidad 'p' de que un hijo sea como su padre (en tanto por uno):", padding="0 15 0 0")                               
        self.entry1_p =ttk.Entry(self, textvariable=self.p, width=60)    
        self.entry1_p.focus()                                                        
       
        self.label2_k = ttk.Label(self, style="Normal.TLabel", text="Número 'k' de hijos que al menos quieres que sean como su padre:", padding="0 5 0 0")
        self.entry2_k = ttk.Entry(self, textvariable=self.k, width=60)

        self.label3_prob_error_P = ttk.Label(self, style="Normal.TLabel", text="Error que asumimos (se suele usar un valor entre 0.05 y 0.01):", padding="0 5 0 0")
        self.entry3_prob_error_P = ttk.Entry(self, textvariable=self.prob_error_P, width=60)

        self.label4_result = ttk.Label(self, style="Res.TLabel", text="Resultado, tamaño mínimo de la población:", padding="0 15 0 0")           
        self.label5_result = ttk.Label(self, style="R.TLabel", textvariable=self.r)

        self.separator1 = ttk.Separator(self, orient="horizontal")
                
        self.button1_calcular = ttk.Button(self, style="Button.TButton", text="Calcular", command=self.calculate)
        self.button2_salir = ttk.Button(self, style="Button.TButton", text="Salir", command=self.master.destroy)

        self.label1_p.pack(side="top", fill="both", expand=True, padx=10, pady=5)
        self.entry1_p.pack(side="top", fill="x", expand=True, padx=10, pady=0)
        self.label2_k.pack(side="top", fill="both", expand=True, padx=10, pady=5)
        self.entry2_k.pack(side="top", fill="x", expand=True, padx=10, pady=0)
        self.label3_prob_error_P.pack(side="top", fill="both", expand=True, padx=10, pady=5)
        self.entry3_prob_error_P.pack(side="top", fill="both", expand=True, padx=10, pady=0)
        self.label4_result.pack(side="top", fill="both", expand=True, padx=10, pady=5)
        self.label5_result.pack(side="top", fill="both", expand=True, padx=10, pady=0)        
        self.separator1.pack(side="top", fill="both", expand=True, padx=10, pady=10)
        self.button1_calcular.pack(side="left", fill="both", expand=True, padx=10, pady=5)
        self.button2_salir.pack(side="right", fill="both", expand=True, padx=10, pady=5)  


    def calculate(self):             
        error_data_entry = False
        n=0
        result_final=1
        try:
            p = Decimal(float(self.p.get()))
            prob_error_P = Decimal(float(self.prob_error_P.get()))
            k = int(self.k.get())
            if p<=0 or p>1 or prob_error_P<=0 or prob_error_P>1 or k<=0:
                error_data_entry = True
        except:
            error_data_entry = True

        if not error_data_entry:
            while result_final >= prob_error_P:
                n = n+1
                result_final=0
                for i in range(k):
                    binomial = Decimal(math.comb(n,i))
                    result = binomial * ((1-p)**(n-i)) * p**i
                    result_final = result + result_final
            self.r.set(n)     
        else:
            self.r.set("¡ERROR!")


def win_manual():
    win_menu_manual = Toplevel(root)
    win_menu_manual.focus()
    win_menu_manual.title("Manual")
    win_menu_manual.geometry("1386x732")
    win_menu_manual.resizable(1,1)
    frame_win_menu_manual = ttk.Frame(win_menu_manual, padding= "5 5 5 5")
    frame_win_menu_manual.pack(expand=True)
    st_manual= ScrolledText(frame_win_menu_manual, width=170, height=45)
    st_manual.tag_configure("titulo_principal", font=("Helvetica", 18, "bold"))
    st_manual.tag_configure("titulo_secundario", font=("Helvetica", 14, "bold"))
    st_manual.tag_configure("texto_normal", font=("Helvetica", 11))
    st_manual.insert("1.0", "MANUAL CALCPOPULATIONMIN v.1.0", ("titulo_principal"))
    st_manual.insert("end", "\n\nIntroducción", ("titulo_secundario"))
    st_manual.insert("end", "\n\nLa aplicación 'CalcPopulationMin' sirve para calcular el tamaño mínimo de la población que sería necesaria para que al menos un número 'k' de hijos tengan el mismo genotipo que su padre para un carácter en concreto del cual conocemos su frecuencia de combinación de genes 'p'.", ("texto_normal"))
    st_manual.insert("end", "\n\nEste es un problema típico de genética cuantitativa. Para solucionar este problema es necesario resolver la siguiente ecuación:\n\n\n", ("texto_normal"))
    st_manual.image_create("end", image=photo_equation)
    st_manual.insert("end", "\n\ndonde:\n", ("texto_normal"))
    st_manual.insert("end", "\n           p = Probabilidad 'p' de que un hijo sea como su padre, frecuencia de combinación de genes.", ("texto_normal"))
    st_manual.insert("end", "\n           k = Número 'k' de hijos que al menos quieres que sean como su padre.", ("texto_normal"))
    st_manual.insert("end", "\n           P = Error que asumimos.", ("texto_normal"))
    st_manual.insert("end", "\n           N = Tamaño mínimo de la población necesaria.", ("texto_normal"))
    st_manual.insert("end", "\n\n\nComo se puede observar, resolver esta ecuación de forma manual se vuelve inviable para un número 'k' alto. Esta es la razón de la existencia de esta aplicación informática, ahora con esta calculadora puedes obtener el resultado de una forma más rápida.", ("texto_normal"))
    st_manual.insert("end", "\n\n\nAspectos a tener en cuenta al realizar el cálculo", ("titulo_secundario"))
    st_manual.insert("end", "\n\nPara realizar un cálculo con la aplicación es interesante que tengas en cuenta los siguientes aspectos:", ("texto_normal"))
    st_manual.insert("end", "\n\n1. Para la primera entrada de datos denominada \"Probabilidad 'p' de que un hijo sea como su padre\" se debe introducir la probabilidad en tanto por uno, es decir, un valor mayor que 0 y menor o igual a 1.", ("texto_normal"))
    st_manual.insert("end", "\nSi se introduce un valor diferente, al pulsar el botón calcular, se mostrara como resultado el texto ¡ERROR!.", ("texto_normal"))
    st_manual.insert("end", "\n\n2. Para la segunda entrada de datos denominada \"Número 'k' de hijos que al menos quieres que sean como su padre\" se debe introducir cualquier valor entero mayor que 0.", ("texto_normal"))
    st_manual.insert("end", "\nSi se introduce un valor decimal el programa solo tendrá en cuenta la parte entera, por ejemplo, el valor 2.7 será interpretado únicamente como el número entero 2.", ("texto_normal"))
    st_manual.insert("end", "\nSi se introduce un valor diferente, al pulsar el botón calcular, se mostrara como resultado el texto ¡ERROR!.", ("texto_normal"))
    st_manual.insert("end", "\n\n3. Para la tercera entrada de datos denominada \"Error que asumimos\" se debe introducir la probabilidad del error que asumimos en tanto por uno, es decir, un valor mayor que 0 y menor o igual a 1.", ("texto_normal"))
    st_manual.insert("end", "\nSi se introduce un valor diferente, al pulsar el botón calcular, se mostrara como resultado el texto ¡ERROR!.", ("texto_normal"))
    st_manual.insert("end", "\n\n4. Para resolver el coeficiente binomial de la ecuación el programa debe calcular el factorial de 'N' y 'k' en diversas ocasiones (hasta encontrar una 'N' válida que cumpla la condición de la ecuación). Resolver el factorial de números grandes es una operación muy larga que requiere de mayor tiempo de cálculo.", ("texto_normal"))
    st_manual.insert("end", "\n\nA continuación, se exponen los tiempos que han sido necesarios para conseguir el resultado de diferentes cálculos, obtenidos con un PC que dispone de una CPU de 3.60 GHz y 16 GB de memoria RAM:", ("texto_normal"))
    st_manual.insert("end", "\n\n    - Para p=0.3; k=100;   Error=0.01 --> N=402   --> Tiempo necesario de menos de 1 segundo.", ("texto_normal"))
    st_manual.insert("end", "\n    - Para p=0.3; k=300;   Error=0.01 --> N=1117 --> Tiempo necesario de 7 segundos.", ("texto_normal"))
    st_manual.insert("end", "\n    - Para p=0.3; k=500;   Error=0.01 --> N=1816 --> Tiempo necesario de 43 segundos.", ("texto_normal"))
    st_manual.insert("end", "\n    - Para p=0.3; k=1000; Error=0.01 --> N=3543 --> Tiempo necesario de 8 minutos y 53 segundos.\n", ("texto_normal"))
    st_manual["state"] = "disabled"
    st_manual.pack(expand=True, fill="both", side="left")


def win_license():
    win_menu_license = Toplevel(root)
    win_menu_license.focus()
    win_menu_license.title("Licencia")
    win_menu_license.geometry("700x780")
    win_menu_license.resizable(1,1)
    frame_win_menu_license = ttk.Frame(win_menu_license, padding="5 5 5 5")
    frame_win_menu_license.pack(expand=True)
    st_license= ScrolledText(frame_win_menu_license, width=90, height=48)
    st_license.pack(expand=True, fill="both", side="left")
    file_license = open(resource_path("LICENSE.txt"), "r")
    text_license = file_license.read()
    st_license.insert("1.0", text_license)
    st_license["state"] = "disabled"


def win_acerca_de():
    messagebox.showinfo(title="Acerca de...", message="Versión 1.0\nSistema Operativo: Windows 10 (64 bits)\n\nProgramado con Python 3.9.5\nEmpaquetado con PyInstaller 4.5.1\nInterfaz gráfica Tcl/Tk 8.6.9\n\nAutor: Cristian Escrihuela Benages\ne-mail: cristian.escrihuela@gmail.com")


def resource_path(relative_path):    
    try:       
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


if __name__ == "__main__":
    root = Tk()
    photo_equation = PhotoImage(file=resource_path("./equation_population_min.gif"))

    menubar=Menu(root)
    root.config(menu=menubar)
    help_menu = Menu(menubar, name="help", tearoff=0)
    
    help_menu.add_command(label="Manual", command=win_manual)
    help_menu.add_command(label="Licencia", command=win_license)
    help_menu.add_command(label="Acerca de...", command=win_acerca_de)
    menubar.add_cascade(label="Ayuda", menu=help_menu)

    app = Application(master=root)
    app.master.title("CalcPopulationMin")
    app.master.geometry("430x342")
    app.master.resizable(1,1)
    app.master.iconbitmap(default=resource_path("favicon.ico"))
    app.mainloop()