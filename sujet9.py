from csv import reader
def mainsujet9(src : str) -> None : 
    """
    Donner, pour toutes les communes de naissance des étudiants du groupe, la consommation résidentielle
totale d'électricité en MWh en 2019.
 Diagramme de présentation pour chaque commune de naissance des étudiants du groupe de la
consommation industrielle de gaz entre 2015 et 2020.
Sources :
Fichier : conso-elec-gaz-annuelle-par-secteur-dactivite-agregee-commune.zip
URL : https://www.data.gouv.fr/fr/datasets/consommation-annuelle-delectricite-et-gaz-parcommune-et-par-secteur-dactivite/
    """
    communes = {"Voiron":0, "Cellieu":0, "Roussillon":0, "CA Valence Romans Agglo":0}                           #CA Valence Romans Agglo correspond à Romans-sur-Isère
    with open(src, "r") as raw_database: #on ouvre puis stocke le fichier
        database = reader(raw_database,delimiter=';')                                                           #on sépare en différentes catégories
        for line in database:                                                                                   #line -> list()
            if line[1]=="2019" and line[26] in communes:                                                        #26 correspond à la catégorie libellé de la commune
                communes[line[26]] = float(line[3])+float(line[7])+float(line[11])                              #consoa, consoi et consot sont aux rangs respectifs 3, 7 et 11
    print(communes.items())                                                                                     #on renvoie les keys et les values sous une liste