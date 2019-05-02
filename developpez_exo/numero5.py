print("Combien de division par 2")
num = int(input("Entrez un entier positif :"))
number = num

while num < 1:
    num = int(input("Entrez un entier positif !:"))

i = 0
while num%2 == 0:
    num = num / 2
    i += 1

print(number, "est divisible ", i, "fois par 2")