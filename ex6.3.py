# In termini ricorsivi, una parola è un palindromo se la prima e l'ultima lettera sono uguali 
# e ciò che resta in mezzo è un palindromo.

# Quelle che seguono sono funzioni che hanno una stringa come parametro e restituiscono 
# rispettivamente la prima lettera, l'ultima lettera, e quelle in mezzo:

def prima(parola):
    return parola[0]

def ultima(parola):
    return parola[-1]

def mezzo(parola):
    return parola[1:-1]

# Scrivete una funzione di nome palindromo che riceva una stringa come argomento e restituisca
# True se è un palindromo e False altrimenti

def palindromo(parola):
    if len(parola) <= 1:
        return True
    if prima(parola) != ultima(parola):
        return False
    return palindromo(mezzo(parola))

print(palindromo('radar'))