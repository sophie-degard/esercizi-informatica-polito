"""Briscola"""

briscola = input ("Seme di briscola: ")
carta1 = input ("Carta primo giocatore: ") 
carta2 = input ("Carta secondo giocatore: ") 

seme1 = carta1[1]
seme2 = carta2[1]

valore1 = carta1[0]
valore2 = carta2[0]

ordine_crescente = "24567JQK3A" #indice per la scala di valori
# le posizioni di indici maggiori corrispondono a carte di valore maggiore 
ordine1 = ordine_crescente.find(valore1) 
ordine2 = ordine_crescente.find(valore2)

# TODO: verificare la correttezza dei dati di ingresso

#calcolo i vincitori
# c'è una briscola 
if seme1 == briscola and seme2 != briscola:
    vincitore = carta1
elif seme2 == briscola and seme1 != briscola:
    vincitore = carta2
elif seme1 != seme2: 
    vincitore = carta1
else:
    #se arrivo qui so di sicuro che seme1=seme2
    if ordine1 > ordine2:
        vincitore = carta1
    else :
        vincitore = carta2 

# Risultato 
print (f"Vince: {vincitore}")

"""
Ordine lessicografico non va bene 
2 3 4 5 6 7 A J K Q

STRATEGIA
converto valori in ordine
2 -> 1 
4 -> 2
5 -> 3
6 -> 4
7 -> 5
J -> 6
Q -> 7
K -> 8
3 -> 9
A -> 10

"""