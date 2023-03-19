from Config import config
import random

hauteur = config["map"]["hauteur"]
largeur = config["map"]["largeur"]

nombre_de_cases = (largeur - 2) * (hauteur - 2)


ressources = []
for type, taux in config["ressources"]["types"].items() :
    nombre_de_ressources = round(taux * nombre_de_cases / 100)
    ressource_actuelle = 1
    while ressource_actuelle <= nombre_de_ressources :
        ressource = {
            "type" : type,
            "quantite" : random.randint(config["ressources"]["quantite"]["min"],config["ressources"]["quantite"]["max"]),
            "position" : [
                random.randint(2, largeur - 1),
                random.randint(2, hauteur - 1)
            ]
        }
        ressources.append(ressource)
        ressource_actuelle = ressource_actuelle + 1



def recuperer_ressource(x,y):
    for ressource in ressources :
        position = ressource["position"]
        if position[0] == x and position[1] == y :
            return ressource["type"][0]
    return " "
