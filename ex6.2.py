"""
La funzione di Ackermann, A(m, n), è così definita:
          { n + 1                  se m = 0
A(m, n) = { A(m - 1, 1)            se m > 0 e n = 0
          { A(m - 1, A(m, n - 1))  se m > 0 e n > 0.
          
Scrivete una funzione di nome ack che valuti la funzione di Ackermann. Usate la vostra funzione per calcolare 
ack(3, 4), vi dovrebbe risultare 125.

Cosa succede per valori maggiori di m e n?
"""

def ack(m, n):
    if m == 0:
        return n + 1
    if n == 0:
        return ack(m - 1, 1)
    return ack(m - 1, ack(m, n - 1))

print(ack(3, 4))
