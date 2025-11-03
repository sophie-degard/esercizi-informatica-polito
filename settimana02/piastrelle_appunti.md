# Es. Piastrelle

## Consegna
*Bisogna posizionare lungo il muro una fila di piastrelle nere e bianche.
Per ragioni estetiche l'architetto ha specificato che la prima e l'ultima piastrella devono essere nere (e le piastrelle alternata).
Il vostro compito è calcolare il numero delle piastrelle della riga, 
dato lo spazio disponibile e la larghezza*

## Appunti

Muro = 1.2 mt = 120 cm 
Piastrella = 25 cm 

Quante piastrelle?
120/25: 3 piastrelle

Quante nere?
2 nere

Quante bianche?
1 bianca

Spazio vuoto?
(120-75)/2 = 45/2 cm = 22.5 per lato

Qual è il numero minimo di piastrelle?
3 o 1?

---

## Algoritmo 1

### Input
    MURO = larghezza del muro in cm 
    PIASTRELLA = larghezza piastrella in cm 

### Output
    n_piastrelle (numero totale di piastrelle) 
    n_nere (numero di piastrelle nere)
    n_bianche (numero di piastrelle bianche)
    vuoto (spazio vuoto da ciascuno dei lati in cm) -> può essere zero

### Vincoli
    Le piastrelle devono essere di colori alternati
    Deve esserci almeno 1 piastrella totale 

### Algoritmo
Cerco il numero intero più vicino per difetto ad x 
1. x = MURO // PIASTRELLA 
    - ottengo 
2. n_piastrelle = int(x) - (1 - (int(x) % 2))
    - (1-(int(x) % 2)) --> è un'espressione che mi dà 1 se x è dispari e 0 se x è pari

---

## Algortimo 2 
    coppie_bn = (MURO - PIASTRELLA) // (2*PIASTRELLA)
    piastrella nera + coppie bianca/nera 

n_bianche = n_coppie
n_nere = n_bianche + 1 
