n = int(input("Entrez un entier strictement positif :"))
while n < 1:
    n = int(input("Entrez un entier STRICTEMENT POSITIF, s.v.p. :"))

div = []

for i in range(2,n):
    if n%i == 0:
        div.append(i)



if not div:
    print(n, "est premier")
else :
    print("diviseur propre de 12", div, "soit %s diviseurs" %(len(div)))