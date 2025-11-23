"""
Esercizi ciclo while
"""

# Stampa i quadrati di tutti i numeri che l'utente 
# inserisce da tastiera
# finché l'utente non inserisce il valore zero 

numero = int(input ("Inserisci numero: "))

while numero != 0 : 
    quadrato = numero ** 2
    print (numero, quadrato)
    numero = int(input ("Inserisci numero: "))

print ("Fine")

# PRINCIPIO DRY = DON'T REPEAT YOURSELF