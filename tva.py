
liste_prod = []

class Produit():
    def __init__(self, nom_art:str, desc:str, taux, prixT:float, prixH:float):
        self.nom_art = nom_art
        self.desc = desc
        self.tva = taux
        self.prixH = prixH
        self.prixT = prixT

    
    def prix_ttc(self,tx:float):
        self.prixT = float(self.prixH) + (float(self.prixH)*tx)

def creer_pro():
    print("======================================== CREER UN PRODUIT ========================================")
    n = input('Nom du produit: ')
    d = input('Description du produit: ')
    t = input('Choisir le taux t1 = 20%, t2 = 5.5% et t3 = 2.1%: ')
    if t == 't1':
        taux = 0.2
    elif t == 't2':
        taux = 0.05
    elif t == 't3':
        taux = 0.021
    p = input('Prix hors taxe: ')
    pt = 0
    i = 'p'+ str(len(liste_prod))
    i = Produit(n, d, t, pt, p)
    i.prix_ttc(taux)
    liste_prod.append(i)
    menu()

def menu():
    print("======================================== MENU ========================================")
    x = int(input("Choisir l'action a effectué: \n 1. Créer un produit \n 2.Voir la liste des produits \n 3. Modifier un produit \n"))
    if x ==1:
        creer_pro()
    elif x == 2:
        liste()
    elif x == 3:
        modifier()
    else:
        print('Erreur veuillez saisir la meilleure option')

def liste():
    print("======================================== LISTE DES PRODUITS ========================================")
    if liste_prod == []:
        print('Aucun Produit')
    else:
        for produit in liste_prod:
            i = 1
            print(str(i)+'. '+ produit.nom_art+' \n   '+produit.desc+' \n   '+str(produit.prixT)+' fc')
            i+=1
            print("************************************************************ \n  \n")
    menu()
    
def modifier():
    print("======================================== MODIFIER UN PRODUIT ========================================")
    indice = input("Entrer le nom de l'article: ")
    for produit in liste_prod:
            if produit.nom_art == indice:
                print(produit.nom_art+' \n   '+produit.desc+' \n   '+str(produit.prixT)+' fc')
                x = int(input("Choisir l'action a effectué: \n 1. Changer le nom \n 2.Changer de description \n 3. Changer le taux de la TVA \n"))
                if x ==1:
                    n = input('Nouveau nom: ')
                    produit.nom_art = n
                    print(produit.nom_art+' \n   '+produit.desc+' \n   '+str(produit.prixT)+' fc')
                elif x == 2:
                    n = input('Nouvelle description: ')
                    produit.desc = n
                    print(produit.nom_art+' \n   '+produit.desc+' \n   '+str(produit.prixT)+' fc')
                elif x == 3:
                    n = input('Choisir le taux t1 = 20%, t2 = 5.5% et t3 = 2.1%: ')
                    if n == 't1':
                        taux = 0.2
                    elif n == 't2':
                        taux = 0.05
                    elif n == 't3':
                        taux = 0.021
                    produit.prix_ttc(taux)
                    print(produit.nom_art+' \n   '+produit.desc+' \n   '+str(produit.prixT)+' fc')
                else:
                    print('Erreur veuillez saisir la meilleure option')
                break
            else:
                print("Ce produit n'existe pas")
            menu()

print("======================================== BIENVENU ========================================")
print("****************************************************************")
menu()
