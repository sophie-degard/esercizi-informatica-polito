# Il saldo di un conto bancario dopo il primo, secondo e terzo anno. 
# Il conto ha un saldo iniziale di 1000 dollari e vi vengono accreditati interessi annuali al 5%.

S = 1000

for A in range (3) : 

    S = S + S*0.05

    print ("anno ", A + 1, ": ", S, "$")

#provo a stampare usando la stringa formattata
print (f"anno {A + 1}: {S:>20.10f}")