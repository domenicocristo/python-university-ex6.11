"""
Un numero, a, è una potenza di b se è divisibile per b e a/b è a sua volta una potenza di b.

Scrivete una funzione di nome potenza che prenda come parametri a e b e che restituisca True 
se a è una potenza di b. Nota: dovete pensare bene al caso base.
"""
def potenza(a, b):
    if a == b:
        return True
    elif a < b or a % b != 0:
        return False
    else:
        return potenza(a/b, b)

print(potenza(16, 2))
