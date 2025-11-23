"""03.1.1 Vero o Falso. 
Per ciascuna delle seguenti coppie di valori, 
eseguire un test di uguaglianza, assegnare il risultato ad una variabile, 
e visualizzarlo. Provare a prevedere quale sarà il risultato di ciascuna verifica.

    I. 1, 1;
    II. 1, 1.0;
    III. 2.0, sqrt(4);
    IV. '1', 1;
    V. 'ciao', 'Ciao'.

"""
from math import sqrt

#prima coppia
a = 1
b = 1

test = a == b 
print (f"{a} è di tipo {type(a)}")
print (f"{b} è di tipo {type(b)}")

if test is True:
    print (f"{a} è uguale a {b}")
else :
    print (f"{a} è diverso da {b}")

#seconda coppia
print ("-"*50)
a = 1
b = 1.0

test = a == b 
print (f"{a} è di tipo {type(a)}")
print (f"{b} è di tipo {type(b)}")

if test is True:
    print (f"{a} è uguale a {b}")
else :
    print (f"{a} è diverso da {b}")

#terza coppia
print ("-"*50)
a = 2.0
b = sqrt(4)

test = a == b 
print (f"{a} è di tipo {type(a)}")
print (f"{b} è di tipo {type(b)}")

if test is True:
    print (f"{a} è uguale a {b}")
else :
    print (f"{a} è diverso da {b}")

#quarta coppia
print ("-"*50)
a = '1'
b = 1

test = a == b 
print (f"{a} è di tipo {type(a)}")
print (f"{b} è di tipo {type(b)}")

if test is True:
    print (f"{a} è uguale a {b}")
else :
    print (f"{a} è diverso da {b}")

#quinta coppia
print ("-"*50)
a = "ciao"
b = "Ciao"

test = a == b
print (f"{a} è di tipo {type(a)}")
print (f"{b} è di tipo {type(b)}")

if test is True:
    print (f"{a} è uguale a {b}")
else :
    print (f"{a} è diverso da {b}")

