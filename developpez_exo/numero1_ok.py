# -*- coding : utf8 -*-


import math

def circle_area(r):
    """calcul la surface d'un cercle de rayon (r). Return la surface"""

    area = math.pi * (r * r)
    print("Aire de la base: ", area, unit+"2")

    return area

def cone_volum(h, r):
    """calcul le volume du cone de base (r) et hauteur (h), appel la fct circle_area(r). return le volume.
    les unités doivent etres cohérentes"""

    base_area = circle_area(r)
    volum = (base_area * h) / 3

    return volum


h = float(input("Entrez la hauteur: "))
r = float(input("entrez le rayon: "))
unit = input("entrez l'unité: ")


print("Volume du cone :", str(cone_volum(h, r)), unit + "3")