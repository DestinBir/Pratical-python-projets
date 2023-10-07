
# ---------------------------------------------------------

allergene = ["piment", "fumée", "pollen", "fourrure", "froid", "poussiere", "odeur_forte"]
statut = "rester"


def chercher(el):
    for i in allergene:
        if el == i:
            al = 'oui'
            break
        else:
            al = "non"

    print("Allergie:  ", al)


while statut == "rester":
    entry = input("Entrer l'élément: ")

    print(chercher(entry))

    print("Merci, voulez-vous partir? Si oui taper 'sortir' sinon taper 'rester' ")
    statut = input('    : ')
    print('_______________________________________________________________')