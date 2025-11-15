import tkinter as tk

def conteggio():
    global conta
    conta += 1
    label.config(text=f"Numero click: {conta}") #aggiornamento dell'oggetto

#creazione della finestra
root = tk.Tk()
root.title("Conta Click")
root.geometry("400x200")

#crep il contenitore di base
frm = tk.Frame(root, bg="lightgrey")
frm.pack(padx=5, pady=5, fill="both", expand=True)

#testo
conta = 0
label = tk.Label(frm, text=f"Numero click: {conta}", font=("Arial", 16))
label.pack(pady=20)

#pulsante
button = tk.Button(frm, text="Cliccami!", command=conteggio)
button.pack(pady=10)

#mainloop
root.mainloop()