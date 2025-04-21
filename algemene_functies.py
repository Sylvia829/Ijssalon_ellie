def mijn_functie_1(a = 2, b = 4, c = 10, d = 12):
    return a * a, b * b, c * c, d * d
totaal = mijn_functie_1()
print(totaal)
def decoreer(tekst""):
def mijn_functie_2(a=12, b=3, c=12, d=2, e=10, f=5, g=100, h=20):
    uitvoer_lijst = []
    uitvoer_lijst.append(a+b)
    uitvoer_lijst.append(c+d)
    uitvoer_lijst.append(e+f)
    uitvoer_lijst.append(g+h)
    uitvoer_lijst.append(a-b)
    uitvoer_lijst.append(c-d)
    uitvoer_lijst.append(e-f)
    uitvoer_lijst.append(g-h)
    uitvoer_lijst.append(a*b)
    uitvoer_lijst.append(c*d)
    uitvoer_lijst.append(e*f)
    uitvoer_lijst.append(g*h)
    uitvoer_lijst.append(a/b)
    uitvoer_lijst.append(c/d)
    uitvoer_lijst.append(e/f)
    uitvoer_lijst.append(g/h)
    return uitvoer_lijst
totaal2 = mijn_functie_2()
print(totaal2)
