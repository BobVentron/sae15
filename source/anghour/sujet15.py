import csv
from gestion.gestionConfig import recupDonneeEtudiant
from gestion.gestionWeb import modifierWeb

def mainsujet15(src : str, cheminData : str) -> tuple:
    """Searches for and add to a web page the watercourses for the specified municipalities. The function also searches the number of dry watercourses and total watercourses of each birth departement of the member of the group.
    Parameters:src (str): The path to the CSV file containing watercourse records. chelinData: path to the data folder containing the "configuration" file.
    Returns:Tuple"""
    try : 
        with open(src, newline='', encoding='utf-8') as csvFile:
            cours_eau_data = csv.reader(csvFile, delimiter=',')
            next(cours_eau_data)  # Skip the first line (header) of the CSV file
            codes_postaux_interet = recupDonneeEtudiant(f"{cheminData}/configuration.txt", "codePostaux")
            dico = {};dico_diagramme_totaux = {};dico_diagramme_asec = {}
            for lignes in cours_eau_data :
                dico[lignes[12]] = lignes[1]
                mois = (lignes[4])[5:7]
                for code in codes_postaux_interet:
                    if (str(lignes[12]))[:2] == (str(code))[:2]: 
                        indice = f"{(str(code))[:2]}/{mois}"
                        if not indice in dico_diagramme_totaux : 
                            dico_diagramme_totaux[indice] = 0
                            dico_diagramme_asec[indice] = 0
                        dico_diagramme_totaux[indice] += 1
                        if lignes[5] == "Assec":
                            dico_diagramme_asec[indice] += 1
            for code in codes_postaux_interet:
                original_code = code
                while str(code) not in dico and code < 100000:
                    code += 1
                    if str(code) in dico:
                        print(f"le cours d'eau le plus près du code postal {original_code} est: {dico[str(code)]}")
                        modifierWeb("./www/anghour.html", "<!--Repere1-->", f"<p>le cours d'eau le plus près du code postal {original_code} est: {dico[str(code)]}</p>")           
            return (dico_diagramme_totaux, dico_diagramme_asec)
    except FileNotFoundError as e: print(f"{src} doesn't exist") #Error in case of an invalid path.
    except PermissionError as e : print(f"You don't have the permissions on {src}") #Error in case of denied permission.
    except TypeError as e: print(f"{src} has the wrong type")  #Error in case of an invalid file type.
    except e: print(e)#Any other error