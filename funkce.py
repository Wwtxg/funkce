def scitani(x, y):
    vysledek = x+y
    return vysledek

promena1 = input("Zadejte promenu 1")
promena2 = input("Zadejte promenu 2")

promena1 = int(promena1)
promena2 = int(promena2)

vysledek = scitani(promena1, promena2)

print ("Vysledek je : " , str(vysledek))