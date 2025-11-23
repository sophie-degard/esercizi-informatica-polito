
"""
Alternativa con controllo anche su piano= 13 / 17
""" 
piano = int(input ("A che piano vuoi andare? "))

if piano == 13 or piano == 17 :
    piano_reale = "ERRORE"
elif piano < 13 :
    piano_reale = piano 
elif piano < 17 : 
    piano_reale = piano - 1
else : 
    piano_reale = piano - 2

print ("Bisogna spostarsi al piano ", piano_reale)