import tkinter as tk

def operazione(testo: str):
    if testo.isdigit():
        #aggiungo al numero
        vecchio_valore = valore.get()
        vecchio_valore += testo
        valore.set(vecchio_valore)
    elif testo==">":
        vecchio_testo = valore.get()
        vecchio_testo = vecchio_testo[:-1]
        valore.set(vecchio_testo)


#main
root = tk.Tk()
root.geometry("400x600")
root.title("Calc9000")

frm = tk.Frame(root, bg="white")
frm.pack(fill="both", expand=True)

#i due frame principali
frm_superiore = tk.Frame(frm)
frm_superiore.pack(fill="x")

frm_inferiore = tk.Frame(frm)
frm_inferiore.pack()

#gestione del frame superiore
btn_uguale = tk.Button(frm_superiore, text="=")
btn_uguale.grid(row=0, column=0, sticky="W")

valore = tk.StringVar()
schermo = tk.Label(frm_superiore, textvariable=valore)
schermo.grid(row=0, column=1, sticky="NSEW")

frm_superiore.grid_rowconfigure(0,weight=1)
frm_superiore.grid_columnconfigure(0, weight=1)
frm_superiore.grid_columnconfigure(1, weight=3)

#gestione del frame inferiore
pulsanti = [
    ("9",0,0),
    ("8",0,1),
    ("7",0,2),
    ("+",0,3),
    ("6",1,0),
    ("5",1,1),
    ("4",1,2),
    ("-",1,3),
    ("3",2,0),
    ("2",2,1),
    ("1",2,2),
    ("x",2,3),
    (">",3,0),
    ("0",3,1),
    (",",3,2),
    ("/",3,3)
]

for (testo, riga, colonna) in pulsanti:
    btn = tk.Button(frm_inferiore,text=testo, command=lambda t=testo: operazione(t))
    btn.grid(row=riga, column=colonna, sticky="NSWE", padx=5, pady=5)

#mainloop
root.mainloop()