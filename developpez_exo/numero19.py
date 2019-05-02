n = int(input("Entrez un nombre entre 2 et 12 inclus :"))
while n < 2 or n > 12:
    n = int(input("Entrez un nombre entre 2 et 12, s.v.p. :"))

print("Pöur faire un ", n, "les combinaison possible sont :")


dé1, dé2, count = 0,0,0
for i in range(7):
    if n-i <=6 and n-i > 0 and i <=6 and i > 0:
      dé1 = i
      dé2 = n-i

      print("dé N°1: {}. dé N°2: {}".format(dé1,dé2))
      count +=1
print("il y a {} maniere de faire {} avec deux dés".format(count, n))
#################################### correction###############################
# Programme principal =========================================================
"""
n = int(input("Entrez un entier [2 .. 12] :"))
while not(n >= 2 and n <= 12) :
    n = int(input("Entrez un entier [2 .. 12], s.v.p. :"))
    """

s = 0
for i in range(1, 7) :
    for j in range(1, 7) :
        if i+j == n :
            s += 1

print("Il y a {} façon(s) de faire {} avec deux dés.".format(s, n))