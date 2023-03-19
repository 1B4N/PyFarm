from Config import config
from Ressources import recuperer_ressource

def afficher_map():
    hauteur = config["map"]["hauteur"]
    largeur = config["map"]["largeur"]

    ligne_actuelle = 1
    while ligne_actuelle <= hauteur :
        ligne = ''
        colonne_actuelle = 1
        while colonne_actuelle <= largeur:
            if ligne_actuelle == 1 or ligne_actuelle == hauteur or colonne_actuelle == 1 or colonne_actuelle == largeur :
                case = '+'
            else :
                case = recuperer_ressource(colonne_actuelle, ligne_actuelle)
            ligne = ligne + case
            colonne_actuelle = colonne_actuelle + 1
        print(ligne)
        ligne_actuelle = ligne_actuelle + 1
