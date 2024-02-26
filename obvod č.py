def obvod(a, b, c):
    vysledek = a+b+c
    return vysledek

def obsah(c, v):
    vysledek = (c*v)/2
    return vysledek

print ("Pro vypocet obvodu zadejte 1")
print ("Pro vypocet obsahu zadejte 2")

volba = input("Zadejte svoji volbu:")

if volba == "1":
    promenaA = int(input("Zadejte stranu a"))
    promenaB = int(input("Zadejte stranu b"))
    promenaC = int(input("Zadejte stranu c"))
    vysledek = obvod(promenaA, promenaB, promenaC)
    print("Vysledek je: " , vysledek) 
elif volba == "2":
    promenaX = int(input("Zadejte stranu x"))
    promenaVx = int(input("Zadejte vysku  Vx"))
    vysledek = obsah(promenaX, promenaVx)
    print("Vysledek je: " , vysledek) 
else:
    print ("ERROR")