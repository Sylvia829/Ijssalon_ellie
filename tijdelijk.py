aanbieding = 0.8 
keys = "aardbei"
values = 3 
reclame_tekst= "Vandaag in de aanbieding: aardbei-ijs, 1 liter - slechts € <aanbieding>"
aanbieding = (values * aanbieding)
reclame_tekst2 = reclame_tekst [:62]
reclame_tekst3 = "Vandaag in de aanbieding: aardbei-ijs, 1 liter - slechts € 2.4"
reclame_tekst4 = "Vandaag in de aanbieding: aarbeid-ijs, 1 liter - slechts € 2.4"
el = "Vandaag in de aanbieding: aardbei-ijs, 1 liter - slechts € 2.4"
for word in el.split():
    print (word.lower())