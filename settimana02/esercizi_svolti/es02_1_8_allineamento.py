"""
Formattare l’output dell’esercizio 02.1.1 in modo che descrizioni 
e numeri siano allineati verticalmente, ad esempio:
"""

from statistics import mean

COST1 = 15.0
COST2 = 27.0

somma = COST1 + COST2
differenza = COST1 - COST2
prodotto = COST1 * COST2
valore_medio = mean ([COST1, COST2])
distanza = abs (differenza)
massimo = max (COST1, COST2)
minimo = min (COST1, COST2)

print (f"somma:      {somma:10.2f}")
print (f"differenza: {differenza:10.2f}")
print (f"prodotto:   {prodotto:10.2f}")
print (f"media:      {valore_medio:10.2f}")
print (f"distanza:   {distanza:10.2f}")
print (f"massimo:    {massimo:10.2f}")
print (f"minimo:     {minimo:10.2f}")
#f"result: {value:{width}.{precision}}"