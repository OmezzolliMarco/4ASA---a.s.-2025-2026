def trova_prefisso(a:str, b:str):
    #trova
    lunghezza = min(len(a), len(b))
    if lunghezza==0:
        return ""
    prefisso = ""
    for i in range(0, lunghezza):
        if a[i]==b[i]:
            prefisso += a[i]
        else:
            return prefisso

def trova_suffisso(a:str, b:str):
    prefisso = trova_prefisso(a[::-1], b[::-1])
    return prefisso[::-1]


a = input("Inserisci la prima parola: ")
b = input("Inserisci la seconda parola: ")

pref = trova_prefisso(a, b)
suff = trova_suffisso(a, b)
print(f"Prefisso: {pref}, Suffisso: {suff}")