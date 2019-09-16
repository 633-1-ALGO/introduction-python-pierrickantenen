# Consigne : Rechercher le nombre d'occurences du mot "exemple" et l'afficher. Remplacer le mot "est" par "représente".
# Bonus : Inverser le sens de lecture.
texte = "Ceci est un exemple exemplaire d'exemple exempté d'exemple."
texteSplit = texte.split()
cmt = 0;
nouveauTexte = ""
for ligne in texteSplit:
    if "exemple" in ligne:
        cmt+=1
    if ligne == "est":
        ligne = "représente"
    nouveauTexte += ligne
    nouveauTexte += " "
print(cmt)
print(nouveauTexte)
