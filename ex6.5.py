"""
Il massimo comun divisore (MCD) di due interi a e b è il numero intero più grande 
che divide entrambi senza dare resto.

Un modo per trovare il MCD di due numeri si basa sull'osservazione che, se r è il resto della divisione 
tra a e b, allora mcd(a,b) = mcd(b,r). Come caso base, possiamo usare mcd(a,0) = a.

Scrivete una funzione di nome mcd che abbia come parametri a e b e restituisca il loro massimo comun divisore.
"""

def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)

print(mcd(60, 48))
