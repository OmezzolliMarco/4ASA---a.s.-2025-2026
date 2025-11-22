'''
realizza una finestra nella quale è presente una label che 
contiene la scritta "Nascosto" e quando si 
preme un pulsante tale scritta deve cambiare in "Ciao sono [nome]".
'''

import tkinter as tk

#funzioni
def cambiaTesto():
    testo.config(text="Ciao sono Marco")

#main
root = tk.Tk()
root.title("Cambia frase")
root.geometry("400x300")


frm = tk.Frame(root, bg="lightblue")
frm.pack(padx=5, pady=5, fill="both", expand=True)

testo = tk.Label(frm, text="Nascosto")
testo.pack(pady=15)

pulsante = tk.Button(frm, text="Cliccami!",  command=cambiaTesto)
pulsante.pack(pady=20)

#mainloop
root.mainloop()
