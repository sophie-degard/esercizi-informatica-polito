"""
Scrivere lo pseudocodice e il relativo programma Python che aiuta una persona a decidere se comprare o meno un’auto ibrida. 
Gli input del programma dovrebbero essere:

I. il costo di un’auto nuova;

II. la stima dei chilometri percorsi in un anno;

III. La stima del costo del carburante;

IV. L’efficienza in chilometri al litro;

V. La stima del valore di rivendita dell’auto usata dopo 5 anni.

Calcolare il costo totale di proprietà dell’auto per 5 anni 
(per semplicità, non tenere in considerazione il costo di finanziamenti). Per fornire gli input al programma, 
ricercare sul Web prezzi e consumi realistici per due alternative per l’acquisto di un’auto nuova nella stessa fascia di prezzo: 
un modello ibrido e uno a benzina. Eseguire il programma due volte per comparare le due alternative, 
considerando l’attuale prezzo del carburante e la previsione di percorrere 30’000 chilometri all’anno. [P2.10]
"""

KM_ANNO = 40000
COSTO_CARBURANTE = 1.7

# CLIO BENZINA
B_COSTO_AUTO = 18900
B_KM_LITRO = 18.5
B_VALORE_USATO_5Y = 8500

consumi_litri = (KM_ANNO*5) / B_KM_LITRO
spesa_carburante = consumi_litri * COSTO_CARBURANTE 
spesa_auto_5y = (B_COSTO_AUTO + spesa_carburante) - B_VALORE_USATO_5Y
print ("TCO Clio Benzina: ", round(spesa_auto_5y, 2))

# CLIO IBRIDA
I_COSTO_AUTO = 24900
I_KM_LITRO = 23.5
I_VALORE_USATO_5Y = 11000

consumi_litri = (KM_ANNO*5) / I_KM_LITRO
spesa_carburante = consumi_litri * COSTO_CARBURANTE 
spesa_auto_5y = (I_COSTO_AUTO + spesa_carburante) - I_VALORE_USATO_5Y

print ("TCO Clio Ibrida: ", round(spesa_auto_5y, 2))