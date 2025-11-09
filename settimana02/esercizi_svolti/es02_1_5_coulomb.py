"""
Secondo la legge di Coulomb, la forza elettrica (espressa in Newton) tra due particelle cariche con carica, 
rispettivamente, Q 1 e Q 2 , separate da una distanza r, 
è R = (Q1*Q2) / (4 𝜋 𝜀 r) dove 𝜀 = 8.854 * 10 ** -12 Farad / metro. 
Scrivere un programma che calcoli e mostri a video la forza relativa ad una coppia di particelle cariche, 
permettendo all’utente di scegliere i valori Q1 , Q2  (in Coulomb) e r (in metri). [P2.43]
"""

from math import pi

Q1 = 5
Q2 = 6
r = 10
COST = 4 * pi * 8.854 * 10**-12

R = (Q1 * Q2) / (COST * r)

print ("Forza Elettrica: ", R, "Coulomb")