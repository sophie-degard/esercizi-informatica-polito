"""
Bisogna posizionare lungo il muro una fila di piastrelle nere e bianche.
Per ragioni estetiche l'architetto ha specificato che la prima e l'ultima piastrella devono essere nere.
Il vostro compito è calcolare il numero delle piastrelle della riga, 
dato lo spazio disponibile e la larghezza 
"""
import math 

MURO = 120
PIASTRELLA = 25

# numero di piastrelle 
# se non ci fossero vincoli sul colore delle piastrelle
x = MURO // PIASTRELLA

# (1-(int(x)) % 2) -> mi restituisce 1 se il numero è pari, 0 se è dispari
n_totali = int (x) - (1-(int(x)) % 2)

n_nere = math.ceil(n_totali/2)
n_bianche = math.floor(n_totali/2)

print ("Nere: ", n_nere)
print ("Bianche:", n_bianche)

vuoto = (MURO - PIASTRELLA * n_totali) / 2
print ("Spazio vuoto: ", vuoto)