def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs * (1-korting)
    uitvoer = f"Vandaag in de aanbieding: Emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting} euro."
    return uitvoer
print(aanbieding_1("aardbei",4, 0.1))
def inkomsten_totaal(a, b, c, d, e, f, g):
    return a+b+c+d+e+f+g
totaal = inkomsten_totaal(220, 430, 125, 160, 205, 90, 345)
print(totaal)
def inkomsten_totaal(inkomsten, btw = 0.09):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."
week_inkomsten = [220, 430, 125, 160, 205, 90, 345]
print(inkomsten_totaal(week_inkomsten, 0.09))
def laag_en_hoog(mijn_lijst):
    hoogste = max(mijn_lijst)
    laagste = min(mijn_lijst)
    return [hoogste, laagste]
week_inkomsten = [220, 430, 125, 160, 205, 90, 345]
print(laag_en_hoog(week_inkomsten))
def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    aantal = len(mijn_lijst)
    return totaal/aantal
week_inkomsten = [220, 430, 125, 160, 205, 90, 345]
print(gemiddelde(week_inkomsten))
def gemiddelde(inkomsten):
    totaal = sum(inkomsten)
    aantal = len(inkomsten)
    gemiddelde = totaal/aantal
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro."
week_inkomsten = [220, 430, 125, 160, 205, 90, 345]
print(gemiddelde(week_inkomsten))
def laag_en_hoog(lijst):
    hoogste = max(lijst)
    laagste = min(lijst)
    return [laagste, hoogste]
def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)
print (meervoudig([10, 5, 3, 2, 1, 4, 9]))
def combinatie(invoer_lijst2):
    korte_lijst = laag_en_hoog(invoer_lijst2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer