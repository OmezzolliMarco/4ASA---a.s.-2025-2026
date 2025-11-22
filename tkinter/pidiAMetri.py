import tkinter as tk

#funzioni
def convertiPiedi():
    valore = float(piedi.get())
    metri.set(0.3*valore)

#main
root = tk.Tk()
root.title("Piedi -> Metri")
root.geometry("600x400")

frm = tk.Frame(root, bg="lightgreen")
frm.grid(column=0, row=0, sticky="NSEW", padx=5, pady=5)

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

#parte di calcolo
l_piedi = tk.Label(frm, text="Piedi", bg="lightgreen")
l_piedi.grid(column=0, row=0, sticky="W", pady=10, padx=10)

piedi = tk.StringVar()
valore_piedi = tk.Entry(frm, width=10, textvariable=piedi)
valore_piedi.grid(column=0, row=1, sticky="W", padx=10, pady=10)

btn = tk.Button(frm, text="=>", command=convertiPiedi)
btn.grid(row=1, column=1, sticky="NSEW", padx=10, pady=10)

l_metri = tk.Label(frm, text="Metri", bg="lightgreen")
l_metri.grid(column=2, row=0, sticky="E", padx=10, pady=10)

metri = tk.StringVar()
valore_metri = tk.Label(frm, text="", bg="lightgreen", textvariable=metri)
valore_metri.grid(column=2,row=1, sticky="E", padx=10, pady=10)

frm.grid_columnconfigure(0, weight=2)
frm.grid_columnconfigure(1, weight=1)
frm.grid_columnconfigure(2, weight=2)

frm.grid_rowconfigure(0, weight=1)
frm.grid_rowconfigure(1, weight=2)

#mainloop
root.mainloop()