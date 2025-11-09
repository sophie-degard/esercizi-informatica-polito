"""
Lo pseudocodice seguente descrive come trasformare una stringa contenente 
un numero telefonico a dieci cifre (come “4155551212”) in una stringa più facilmente leggibile, 
formattata secondo lo stile statunitense, come “(415) 555–1212”:

I. Prendere la stringa costituita dai primi tre caratteri e circondarla con parentesi tonde 
(questo è il prefisso, detto “area code”);

II. Concatenare il prefisso con la stringa contenente i tre caratteri successivi, 
un trattino e la stringa costituita dagli ultimi quattro caratteri si ottiene 
il numero nel formato richiesto.

Tradurre questo pseudocodice in un programma Python che memorizzi un numero telefonico 
di 10 cifre in una stringa, per poi visualizzarlo nel formato appena descritto. [P2.33]
"""

telefono = "3392164323"

# Prendere la stringa costituita dai primi tre caratteri e circondarla con parentesi tonde 
code = telefono[0:3]

# Concatenare il prefisso con la stringa contenente i tre caratteri successivi, 
# un trattino e la stringa costituita dagli ultimi quattro caratteri si ottiene 
# il numero nel formato richiesto.

print ("(" + code + ")" + telefono[3:6] + "-" + telefono[-4:len(telefono)])

