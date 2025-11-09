"""
Scrivere un programma che memorizzi in una costante un numero intero positivo di cinque cifre (quindi compreso tra 10000 e 99999), 
e visualizzi le singole cifre di cui è composto. 
Ad esempio, avendo il numero 16384, il programma deve visualizzare, su righe separate: 1 6 3 8 4. [P2.16]
"""

C = 18745

#soluzione 1 
cs = str (C)

print ("Soluzione 1 utilizzando le stringhe")
print (cs[0])
print (cs[1])
print (cs[2])
print (cs[3])
print (cs[4])

# Soluzione 2
print ("soluzione 2 utilizzando i numeri")

v = C
c1 = v // 10**4 
v = v % 10**4
c2 = v // 10**3
v = v % 10**3
c3 = v // 10**2
v = v % 10**2
c4 = v // 10
c5 = v % 10

print (c1)
print (c2)
print (c3)
print (c4)
print (c5)

# Soluzione 3: parto dalla cifra alta 
v = C
c0 = v % 10
v = v // 10
c1 = v % 10
v = v // 10
c2 = v % 10
v = v // 10
c3 = v % 10
v = v // 10
c4 = v % 10
v = v // 10

print ("Soluzione 3")
print (c4)
print (c3)
print (c2)
print (c1)
print (c0)

