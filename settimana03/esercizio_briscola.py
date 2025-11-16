"""Briscola"""

briscola = input ("Seme di briscola: ") # C
carta1 = input ("Carta primo giocatore: ") # "3P"
carta2 = input ("Carta secondo giocatore: ") # "4C"

seme1 = carta1[1]
seme2 = carta2[1]

numero1 = carta1[0]
numero2 = carta2[0]

# TODO: verificare la correttezza dei dati di ingresso

# c'è una briscola 
if seme1 == briscola and seme2 != briscola:
    vincitore = carta1
elif seme2 == briscola and seme1 != briscola:
    vincitore = carta2
elif seme1 == seme2 : 
    vincitore = 

# ci sono due semi uguali
if 

# Risultato 
print (f"Vince: {vincitore}")

