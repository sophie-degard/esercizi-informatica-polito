""" ESERCIZIO CICLO WHILE 1 
Stampa i quadrati di tutti i numeri che l'utente 
inserisce da tastiera finché l'utente non inserisce il valore *
"""

risposta = input ("Risposta: ")

while risposta != "*" :
    numero = int(risposta)
    quadrato = numero ** 2 
    print (numero, quadrato)
    risposta = input ("Risposta: ")

print ("FINE")

