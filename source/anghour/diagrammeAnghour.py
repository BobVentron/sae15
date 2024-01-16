import matplotlib.pyplot as plt

def sujet15Graph(src: str, tuple_diagrame: tuple) -> None:
    """
    This method creates a diagramm of the percentage of dry streams, per month, for the birth departments of the group members.
    It takes for parameter, a string wich is the path to the CSV files containing the data and a tuple containing the lists created by the function "mainsujet15".
    It doesn't return anything.
    """
    try:
        (dico_diagramme_totaux, dico_diagramme_assec) = tuple_diagrame
        dico_diagramme_final = {}
        for elem in dico_diagramme_totaux:
            dico_diagramme_final[elem] = (int(dico_diagramme_assec.get(elem)) / int(dico_diagramme_totaux.get(elem)))*100
        plt.subplots(figsize=(18,6))
        plt.tick_params(axis='x', labelsize=8)
        plt.bar(dico_diagramme_final.keys(), dico_diagramme_final.values(), color='blue')
        plt.xlabel('Numéro des departements/ numéro du mois'); 
        plt.ylabel('Pourcentage de cour d\'eau à sec'); 
        plt.title(f"")
        plt.savefig(f"./www/medias/GraphAnghour")
    except FileNotFoundError as e:
        print(f"{src} doesn't exist")
    except PermissionError as e:
        print(f"You don't have the permissions on {src}")
    except Exception as e:
        print(e)
