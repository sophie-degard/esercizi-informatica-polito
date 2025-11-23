""" ESERCIZIO CICLO WHILE 3 
Stampare 10 parole casuali di lunghezza compresa tra 5 e 10 lettere ciascuna 
sggerimento: random.random, ord, chr 
"""
import random 

# 1. stabilisco una lunghezza casuale
i = 0 

while i <= 10:                          # fai 10 stringhe casuali
    lunghezza = random.randint(5, 10)
    s = ""
    while len(s) < lunghezza:           # costruisci una stringa casuale
        alfabeto = "abcdefghijklmnopqrstuvwxyz"         # scelgo una lettera random dell'alfabeto
        posizione = random.randint(0,len(alfabeto)-1)     # 
        lettera = alfabeto[posizione]                   # 
        s = s + lettera
    print (s)
    i = i + 1

print ("FINE")