from csv import reader#Importation des bibliothèques
import matplotlib.pyplot as plt
from gestion.gestionConfig import recupDonneeEtudiant

def sujet18Part2(src, cheminData)->list:
    """
    This method gives, for each birth departement of the members of the group, the rent indicator of the different communes.
    It takes a string as parameter wich is the path to the CSV file containing the data to extract.
    The method return a list who contains, for each birth departement of the members of the groupe, the rent indicator of the different communes
    """
    try:
        dico_dep={}
        
        for e in recupDonneeEtudiant(f"{cheminData}/configuration.txt", "codePostaux"):
            dico_dep[(str(e))[:2]]=[]
        
        with open(src, encoding='utf-8') as observations:#Extraction of the data of the CSV file.
            lignesCSV=reader(observations, delimiter=';')
            next(lignesCSV)
            for lines in lignesCSV:
                truc =(lines[1])[:2]
                for k in dico_dep:
                    if truc==k:
                        indicateur=lines[6].replace(",",".")
                        indic=float(indicateur)
                        dico_dep[k].append(indic)
            for k in dico_dep:    
                dico_dep[k].sort()
            return dico_dep
    except FileNotFoundError as e: #Error in case of an invalid path.
        print(f"{src} doesn't exist") #Display an error message.
    except PermissionError as e : #Error in case of denied permission.
        print(f"You don't have the permissions on {src}") #Display an error message.
    except TypeError as e: #Error in case of an invalid file type.
        print(f"{src} has the wrong type 2") #Display an error message.
    except e: #Any other error
        print(e) #Display an error message.
    
def sujet18Graph(src, cheminData)-> None:
    """
    This method makes, for each birth departement of the members of the group, a Graph of the number of commune in function of the rent indicator.
    It takes a string as parameter wich is the path to the CSV file containing the data to extract.
    The method doesn't returns anything, it just makes graphs.
    """
    try:
        dep=""
        data=sujet18Part2(src, cheminData)
        for k in data:
            match k:
                case "38":
                    dep="Isere"
                case "26":
                    dep="Drome"
                case "42":
                    dep="Loire"
            dico={}
            for i in data[k]:
                prix1=min(data[k])
                while prix1 <= max(data[k]):
                    prix2=prix1+0.5
                    if i >= prix1 and i < prix2:
                        dico[f"{prix2:.2f}"]=dico.get(f"{prix2:.2f}",0)+1
                    prix1=prix2
            plt.subplots(figsize=(15,6))
            plt.bar(dico.keys(), dico.values(), color='blue')
            plt.xlabel('Indicateur de loyer (en €/m2)'); plt.ylabel('nb de commune'); plt.title(f"Nombre de communes en fonction de l'indicateur de loyer en {dep}")
            plt.savefig(f"./www/medias/Graph{dep}")
    except FileNotFoundError as e: #Error in case of an invalid path.
        print(f"{src} doesn't exist") #Display an error message.
    except PermissionError as e : #Error in case of denied permission.
        print(f"You don't have the permissions on {src}") #Display an error message.
    except TypeError as e: #Error in case of an invalid file type.
        print(f"{src} has the wrong type 1") #Display an error message.
    except e: #Any other error
        print(e) #Display an error message.