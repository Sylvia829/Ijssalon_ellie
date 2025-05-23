def presenteer (dictonary, totaal):
    mijn_dict = {'vis' : 10, 'vlees' : 25, 'overig' : 15}
    totaal = 50
    for keys, value in dictonary.items():
        print("="*26)
        print(f"totaal = {totaal} euro")