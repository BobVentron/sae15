import matplotlib.pyplot as plt
import numpy as np
from collections import OrderedDict
from soleilhac.sujet17 import mainsujet17

def diagramme(src : str, newCommune : list, listecommune : list)-> None:
    """
    This function allows you to construct the diagram corresponding to subject 17. It takes three parameters but returns nothing
    The first parameter is the path of the csv file corresponding to subject 17.
    the second parameter is a formatted list of municipalities,
    and the last parameter is also a list of municipalities but without formatting.
    """
    try:
        # recovery of the information necessary to create the diagrams
        eleveEnCp = list((mainsujet17(src, newCommune, "cp")).values())
        eleveEnCe1 =  list((mainsujet17(src, newCommune, "ce1")).values())
        eleveEnCe2 =  list((mainsujet17(src, newCommune, "ce2")).values())
        eleveEnCm1 =  list((mainsujet17(src, newCommune, "cm1")).values())
        eleveEnCm2 =  list((mainsujet17(src, newCommune, "cm2")).values())

        categories = list(OrderedDict.fromkeys(listecommune)) # remove duplicates from the list
        donnees = (np.array([eleveEnCp, eleveEnCe1, eleveEnCe2, eleveEnCm1, eleveEnCm2])).T # create a table of the correct format
        couleurs_niveaux = ['red', 'green', 'blue', 'orange', 'purple'] # create a table of the correct format
        fig, ax = plt.subplots(figsize=(10, 6))# Creating the Stacked Bar Chart

        # Using a Loop to Create the Stacked Bars
        for i in range(5):
            if i == 0:
                ax.bar(categories, donnees[:, i], color=couleurs_niveaux[i], label=f'{i+1}')
            else:
                ax.bar(categories, donnees[:, i], bottom=np.sum(donnees[:, :i], axis=1), color=couleurs_niveaux[i], label=f'{i+1}')

        legend = ["Cp", "CE1", "CE2", "CM1", "CM2"] # creation of the list which will serve as a legend
        ax.legend(legend, title='Légende', bbox_to_anchor=(1, 1), loc='upper left') #  creation of the legend
        ax.set_ylabel('Nombre d\'élèves') 
        ax.set_title('Diagramme à barres empilées par commune et par niveau')
        plt.savefig(f"./www/medias/GraphSoleilhac") # we save the graph in the right place
    except FileNotFoundError as e: #Error in case of an invalid path.
        print(f"{src} doesn't exist") #Display an error message.
    except PermissionError as e : #Error in case of denied permission.
        print(f"You don't have the permissions on {src}") #Display an error message.
    except TypeError as e: #Error in case of an invalid file type.
        print(f"{src} has the wrong type 1") #Display an error message.
    except Exception as e: #Any other error
        print(e) #Display an error message.