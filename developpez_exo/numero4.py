print("pair ou impair ?")
num = int(input("Entrez un nombre a tester "))

while num < 1:
    num = int(input("Votre nombre n'est pas un entier positif.\nEntrez un nombre a tester "))

if num % 2 == 0:
    print("il est pair")
else:
    print("il est impair")