"""
Il ciclo while 
"""
# ---------------------------------------------------
# Stampa i numeri da 1 a N con N inserito da tastiera
x = 1           # variabile di controllo

while x <= 10:  # condizione in cui continuare il ciclo
    print (x)   # corpo del ciclo -> posso usare la var di controllo
    x = x + 1   # aggiornamento della variabile di controllo

print ("finito")

# -------------------------------------------
# Stampa i quadrati dei primi N numeri interi

N = int(input("valore di N: ")) # valore di controllo
i = 0 # valore di iterazione

while i < N :              # condizione di iterazione
    quadrato = i**2         
    print (i, quadrato)     # corpo del ciclo
    i =  i + 1              # variabile di aggiornamento

# -------------------------------------------------------
# Stampa i quadrati dei primi N numeri dispari
N = int(input("valore di N: ")) 
i = 0 
numero = 1 

while i < N :              
    quadrato = numero ** 2
    print (numero, quadrato)
    numero = numero + 2
    i = i + 1

