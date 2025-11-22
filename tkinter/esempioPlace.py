import tkinter as tk

#main
root=tk.Tk()
root.title("Place")
root.geometry("400x300")

frm = tk.Frame(root, bg="red")
frm.place(relheight=0.4, relwidth=0.4, relx=0.5, rely=0.5, anchor="center")

#mainloop
root.mainloop()