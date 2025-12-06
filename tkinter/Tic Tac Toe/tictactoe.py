import tkinter as tk

#main
root = tk.Tk()
root.geometry("600x400")
root.title("Tic Tac Toe")

#realizzazione della plancia
frm = tk.Frame(root, bg="lightgreen")
frm.pack(fill="both", expand=True)

#inizio la generazione dei pulsanti
for i in range(0, 3):
    for j in range(0, 3):
        btn = tk.Button(frm, text="")
        btn.grid(row=i, column=j, sticky="NSEW")

for i in range(0,3):
    frm.grid_columnconfigure(i, weight=1)
    frm.grid_rowconfigure(i, weight=1)

#mainloop
root.mainloop()