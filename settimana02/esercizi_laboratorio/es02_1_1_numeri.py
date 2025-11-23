"""
Due numeri. 
Scrivere un programma che memorizzi due numeri interi in due costanti definite nel codice, e poi ne visualizzi:
    A. La somma;
    B. La differenza;
    C. Il prodotto;
    D. Il valore medio;
    E. La distanza (cioè il valore assoluto della differenza);
    F. Il valore massimo (cioè il maggiore tra i due);
    G. Il valore minimo (cioè il minore tra i due).
"""
from statistics import mean

COST1 = 15
COST2 = 27

somma = COST1 + COST2
differenza = COST1 - COST2
prodotto = COST1 * COST2
valore_medio = mean ([COST1, COST2])
distanza = abs (differenza)
massimo = max (COST1, COST2)
minimo = min (COST1, COST2)

print ("somma: ", somma)
print ("differenza: ", differenza)
print ("prodotto: ", prodotto)
print ("media: ", valore_medio)
print ("distanza: ", distanza)
print ("massimo: ", massimo)
print ("minimo: ", minimo)
