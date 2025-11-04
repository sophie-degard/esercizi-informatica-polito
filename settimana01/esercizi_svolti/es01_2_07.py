# Il vostro nome all’interno di un rettangolo, utilizzando i caratteri: ¦ - + , come nell’esempio seguente:
# +------+ 
# ¦ Dave ¦ 
# +------+

nome = "Francesca"
lato_sx= "¦ "
lato_dx= " ¦"
cornice = "+-" + (len(nome)*"-") + "-+"

print (cornice)
print (lato_sx + nome + lato_dx)
print (cornice)



