""" ESERCIZIO CICLO WHILE 2
Dato il valore T inserito dall'utente, quanti quadrati dei numeri
interi bisogna sommare per far sì che la somma sia > T?
"""

T = int(input("Inserisci il Totale: "))
somma = 0
i = 0

while somma <= T:
    quadrato = i ** 2 
    somma = somma + quadrato
    print (i, quadrato, "+")
    i = i + 1 

print (f"Mi servono {i-1} quadrati per arrivare a {T}")