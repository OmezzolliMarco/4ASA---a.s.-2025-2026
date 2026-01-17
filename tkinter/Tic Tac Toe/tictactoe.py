import tkinter as tk
#funzioni

def resettaGioco():
    global board, bottoni, player
    player = "X"
    board = [["" for i in range(3)] for j in range(3)]

    #grafica
    generale = tk.PhotoImage(file="tkinter\\Tic Tac Toe\\general.png")
    generale_piccolo = generale.subsample(8,8)
    #inizio la generazione dei pulsanti
    for i in range(0, 3):
        for j in range(0, 3):
            bottoni[i][j].config(image=generale_piccolo)
            bottoni[i][j].image=generale_piccolo

def controllaVincitore():
    global board
    global vittorie
    for v in vittorie:
        (a,b) = v[0]
        (c,d) = v[1]
        (e,f) = v[2]
        if board[a][b] != "" and board[a][b] == board[c][d] == board[e][f]:
            #chi ha riempito queste posizioni ha vinto
            return board[a][b] #ritorna X oppure O
    return None

def gioca(riga:int, colonna:int):
    icona1_originale = tk.PhotoImage(file="tkinter\\Tic Tac Toe\\cat.png")
    icona2_originale = tk.PhotoImage(file="tkinter\\Tic Tac Toe\\dog.png")

    icona1 = icona1_originale.subsample(8,8)
    icona2 = icona2_originale.subsample(8,8)

    global player
    global board
    global bottoni

    if board[riga][colonna] != "":
        return
    
    #giocata
    board[riga][colonna] = player
    #aggiornamento grafico
    if board[riga][colonna]=="X":
        #metto immagine del gatto
        bottoni[riga][colonna].config(image=icona1)
        bottoni[riga][colonna].image = icona1
    else:
        #metto immagine del cane
        bottoni[riga][colonna].config(image=icona2)
        bottoni[riga][colonna].image = icona2
    
    #controllo del vincitore
    vincitore = controllaVincitore()
    if vincitore != None:
        if vincitore == "X":
            print("Vince player 1")
        else:
            print("Vince player 2")
        resettaGioco()

    #controllo del pareggio
    if all(board[i][j]!="" for i in range(3) for j in range(3)):
        print("Pareggio!")
        resettaGioco()

    #cambio del player
    if player=="X":
        player = "O"
    else:
        player = "X"



#main


vittorie = [
    #righe
    [(0,0), (0,1), (0,2)],
    [(1,0), (1,1), (1,2)],
    [(2,0), (2,1), (2,2)],
    #colonne
    [(0,0), (1,0), (2,0)],
    [(0,1), (1,1), (2,1)],
    [(0,2), (1,2), (2,2)],
    #diagonali
    [(0,0), (1,1), (2,2)],
    [(0,2), (1,1), (2,0)]
]

#main
#definizione elementi del gioco
bottoni = []
for i in range(0,3):
    bottoni.append([0,1,2])

player = "X"
board = [["" for i in range(3)] for j in range(3)]
bottoni = [[None for i in range(3)] for j in range(3)]

root = tk.Tk()
root.geometry("600x400")
root.title("Tic Tac Toe")

#realizzazione della plancia
frm = tk.Frame(root, bg="lightgreen")
frm.pack(fill="both", expand=True)

generale = tk.PhotoImage(file="tkinter\\Tic Tac Toe\\general.png")
generale_piccolo = generale.subsample(8,8)
#inizio la generazione dei pulsanti
for i in range(0, 3):
    for j in range(0, 3):
        btn = tk.Button(frm, image=generale_piccolo, command=lambda r=i, c=j: gioca(r,c))
        btn.grid(row=i, column=j, sticky="NSEW")
        bottoni[i][j]=btn

for i in range(0,3):
    frm.grid_columnconfigure(i, weight=1)
    frm.grid_rowconfigure(i, weight=1)

#mainloop
root.mainloop()