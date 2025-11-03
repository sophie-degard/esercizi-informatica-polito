""" 
Per usare le funzioni appartenenti a uno specifico modulo
Prima di tutto includi questa frase in cima al file del tuo programma
"""
import math

# Convert pennies to dollars and cents 
pennies = 1729
dollars = pennies // 100 # calcola il numero dei dollari
cents = pennies % 100 # calcola il numero dei pennies 

print ("I have", dollars, "dollars and", cents, "cents")

#poi puoi usare semplicemente la funzione
x = 3 
y = math.sqrt(x)

print(y)
print(math.pi)
