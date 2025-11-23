"""
Scrivere un programma che memorizzi una stringa in una variabile e, 
a partire da quella variabile, visualizzi i primi tre caratteri della stringa, 
seguiti da tre punti, ancora seguiti dagli ultimi tre caratteri. 
Ad esempio, se la stringa viene inizializzata al valore “Mississippi”, 
il programma deve visualizzare “Mis...ppi”. 
Cosa succede se la stringa è più corta di 6 caratteri? E se è più breve di 3 caratteri? [P2.22]
"""

stringa1 = "Francesca" # stringa con più di 6 caratteri

print (stringa1[0:3], "...", stringa1[-3:len(stringa1)])

stringa2 = "ciao" # stringa più corta di 6 caratteri

print (stringa2[0:3], "...", stringa2[-3:len(stringa2)])

stringa3 = "ab" # stringa come meno di 3 caratteri
print (stringa3[0:3], "...", stringa3[-3:len(stringa3)])
 
