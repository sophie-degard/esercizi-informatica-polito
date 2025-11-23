""" 03.1.2 Identikit della stringa. 
Scrivere un programma che legga una stringa e 
visualizzi i messaggi appropriati, dopo aver verificato se:

    I. contiene soltanto lettere; 
         str.isalpha()
    II. contiene soltanto lettere maiuscole;
        str.isupper()¶
    III. contiene soltanto lettere minuscole;
        str.islower()¶
    IV. contiene soltanto cifre numeriche decimali;
         c.isdecimal()
    V. contiene soltanto lettere e cifre;
    VI. inizia con una lettera maiuscola;
    VII. termina con un punto.
        
"""

stringa = input("Inserisci qui la stringa: ")

print ("La stringa:", stringa)

# I. contiene soltanto lettere;
if stringa.isalpha():
    print ("- contiene soltanto lettere")

# II. contiene soltanto lettere maiuscole;
if stringa.isupper():
    print ("- contiene soltanto maiuscole")

# III.  contiene soltanto lettere minuscole;
if stringa.islower():
    print ("- contiene soltanto minuscole")

# IV.  contiene soltanto cifre numeriche decimali;
if stringa.isdecimal():
    print ("- contiene soltanto cifre numeriche decimali")

# V. contiene soltanto lettere e cifre;
# if :
   # print ("- contiene soltanto lettere e cifre;")