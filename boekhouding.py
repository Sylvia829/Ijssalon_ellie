import csv
from presentatie import *
from helper import inkomsten

inkomsten = [1000, 2000, 1500, 750]
totaal = sum(inkomsten)
print(totaal)

def presenteer(dictionary, totaal):
    for keys, values in dictionary.items():
        print(f"{keys} : {values} euro")
    print("=" * 26)
    print(f"totaal : {totaal} euro")

inkomsten = {
    "Aardbeien-ijs-totaal" : 1000,
    "Vanille-ijs-totaal" : 2000,
    "Chocolade-ijs-totaal" : 1500,
    "Waterijsjes-totaal" : 750
    }


totaal_inkomsten = sum(inkomsten.values())

presenteer(inkomsten, totaal_inkomsten)

with open ('boekhouding.csv', 'w', newline='') as csvfile: 
    for key, value in inkomsten.items(): 
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([key,value])