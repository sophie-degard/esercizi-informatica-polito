"""Metodi stringhe"""

nome = "Francesca"

# .upper() fa CAPSLOCK
nome_gridato = nome.upper() 
print (nome_gridato)

# .lower()
nome_sussurrato = nome.lower()
print(nome_sussurrato)

#voglio che solo l'ultima lettera sia maiuscola
ultima = nome[len(nome)-1]
ultima_maiuscola = ultima.upper()
print (nome[0:len(nome)-1] + ultima_maiuscola)

# .index() ci dice l'indice della prima occorrenza della sottostringa 
indice_a = nome.index("a")
print (indice_a) #in questo caso sul nome "Francesca" la prima "a" è in posizione 2

# .find() come index() ma risponde anche per casi negativi
indice_b = nome.find("b")
print (indice_b) #in questo caso, non essendoci "b" nel nome 

# .strip() toglie gli spazi superflui dalla stringa
parola= " ciao "
parola_stripped = parola.strip()
print (parola_stripped)

#.replace("find", "replace") trova e sostituisce 
parola_alterata = parola.replace("a", "e")
print (parola_alterata)




