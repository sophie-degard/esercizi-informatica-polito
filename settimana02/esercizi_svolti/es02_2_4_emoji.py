""" ESERCIZIO 02.2.4: EMOJI 
Secondo i dati raccolti dall'Unicode Consortium, 
l'organizzazione no-profit responsabile della digitalizzazione delle lingue del mondo, 
le “lacrime di gioia” ( ) rappresentano oltre il 5% di tutte le emoji utilizzate 
(l’unico altro carattere che ci si avvicina è il ). 
Le prime dieci emoji utilizzate in tutto il mondo sono: ....
Quando scambiate messaggi su Telegram 
(o sulla vostra app di messaggistica preferita),
quali sono le tre emoji che voi personalmente usate più di frequente? 
Utilizzando le informazioni sulla codifica Unicode qui raccolte2 , 
scrivere un programma che mostri a schermo, per ciascuna di queste tre emoji:   
    I. la posizione in classifica (rank);
    II. il Numero Unicode;
    III. il Nome Unicode;
    IV. l’emoji stessa.

Formattare l’output in modo che le informazioni relative 
a ciascuna delle tre emoji siano raccolte su una riga, 
e i diversi campi siano allineati verticalmente.
"""
import unicodedata as ud 

emoji1 = "😘"
emoji2 = "😍"
emoji3 = "😊"

# rank 
rank_emoji1 = 7
rank_emoji2 = 9
rank_emoji3 = 10

# print (rank, codice unicode, nome unicode, emoji)
print (
    f"|{'rank':^6}|{'codice':^8}|{'nome':<40}|{'carattere'}|")
print("-"*68)
print (
    f"|{rank_emoji1:^6}|{ord(emoji1):^8X}|{ud.name(emoji1):<40}|{emoji1:8}|")
print(
    f"|{rank_emoji2:^6}|{ord(emoji2):^8X}|{ud.name(emoji2):<40}|{emoji2:8}|")
print(
    f"|{rank_emoji3:^6}|{ord(emoji3):^8X}|{ud.name(emoji3):<40}|{emoji3:8}|")
