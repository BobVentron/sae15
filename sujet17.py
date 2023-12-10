import csv

def mainsujet17(src) -> None : 
    with open(src, encoding='utf-8') as file :
        CommunesNaissance = ["ROMANS-SUR-ISERE", "VOIRON", "CELLIEU"]
        lignesEcole= csv.reader(file, delimiter=';')
        next(lignesEcole)
        result = {communes: 0 for communes in CommunesNaissance}
        for ligne in lignesEcole :
            commune = ligne[4]
            if commune in CommunesNaissance:
                result[commune] += int(ligne[16])
        print(result)