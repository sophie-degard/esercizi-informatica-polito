"""
Ascensore in cui si salta il piano 13
"""
# piano = int(input ("A che piano vuoi andare? "))

# if piano<13: 
#     # caso "reale", quando il piano è < di 13 
#     piano_reale = piano 

# if piano>13:
#     # caso "speciale", quando il piano è > di 13
#     piano_reale = piano - 1

# print ("Bisogna spostarsi al piano ", piano_reale)

"""
 Alternativa con if-else
"""
# if piano<13: 
#     piano_reale = piano 
# else:
#     piano_reale = piano - 1

# print ("Bisogna spostarsi al piano ", piano_reale)

"""
Alternativa con controllo anche su piano=13 
""" 
piano = int(input ("A che piano vuoi andare? "))

if piano<13: 
    piano_reale = piano 
else: # conta per > o = a 13 
    if piano == 13: 
        piano_reale = "PIANO NON VALIDO"
    else: 
        piano_reale = piano - 1 

print ("Bisogna spostarsi al piano ", piano_reale)

if piano == 13 : 
    print ("Non valido")
elif piano < 13 :
    piano_reale = piano
else:
    piano_reale = piano - 1 