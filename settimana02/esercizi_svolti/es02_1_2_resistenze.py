"""
Considerare il circuito seguente. (cfr immagine sul file)
    Si tratta di un circuito in cui una resistenza r1 è collegata in serie al parallelo delle resistenze r2 e r3. 
Scrivere un programma che, a partire dalle resistenze dei tre resistori, immesse in input dall’utente, 
calcoli la resistenza totale, utilizzando la legge di Ohm. [P2.38]
"""

r1 = 100
r2 = 150 
r3 = 300 

r = r1 + (1/(1/r2 + 1/r3))

print ("resistenza totale: ", r, "Ω")

