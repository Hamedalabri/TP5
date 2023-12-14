nom1 = input("Entrez le nom de la première personne : ").upper()
prenom1 = input("Entrez le prénom de la première personne : ").capitalize()

nom2 = input("Entrez le nom de la deuxième personne : ").upper()
prenom2 = input("Entrez le prénom de la deuxième personne : ").capitalize()


if nom1 < nom2 or nom1 == nom2 and prenom1 < prenom2:

 #print(f"personne1: {nom1} {prenom1} , personne2: {nom2} {prenom2}")
    print(f"personne1: {nom1} {prenom1}")
    print(f"personne2: {nom2} {prenom2}")
else:
    print(f"personne2: {nom2} {prenom2}")
    print(f"personne1: {nom1} {prenom1}")

