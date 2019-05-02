

num = []
exit=""

while exit != "q":
    num.append(int(input("Saisisez un nombre: ")))
    exit = input("pour saisir un autre nombre press any key.\nPour quiter pressez Q")
    exit = exit.lower()

total, i, hundred = 0, 0, 0
num.append(0)

while num[i] > 0:

    total += num[i]

    if num[i] >= 100:
        hundred+=1
    i += 1


print ("Somme", total, "\nCompteur", i, "\nCent", hundred)