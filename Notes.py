coef = []
notes = []
valeur = int(input("entrer une valeur: "))

for i in range(valeur):
    chain = input(f"Veuillez entrer la note du module 1 et le coefficient correspondant : ")
    s =chain.split()
    notes.append(float(s[0]))
    coef.append(float(s[1]))


for i in range(len(notes)):
   print("la note", i , "vaut" , notes[i])
 
 
somme  = 0
sommecoef = 0
moyenne = 0
fin = 0

for i in range(len(notes)):
    somme += notes[i] * coef[i]
    sommecoef += coef[i]

moyenne = somme / sommecoef    

print(f"moyenne: {moyenne}")

