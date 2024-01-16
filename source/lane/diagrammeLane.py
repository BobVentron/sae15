import matplotlib.pyplot as plt
from lane.sujet2 import mainsujet2
from gestion.gestionConfig import recupDonneeEtudiant

def sujet2Graph(src : str, CheminData : str) -> None:
    """
    This function creates an Histogram of the hits for student in the group. 
    1 bar by time slot for each student. 
    This function uses the results of the 'mainsujet2' function to do so.
    It doesn't return anything and doesn't have any parameter.
    """
    try: # This is bassicaly an error tester. The program will work if no error is found.
        listelogin = recupDonneeEtudiant(f"{CheminData}/configuration.txt", "login")
        graphdata = mainsujet2(src,listelogin,"a")  # This line obtains results using the mainsujet2 function and puts them into the 'graphdata' variable
        
        result1, result2 = graphdata  # This line unfolds the results
            
        # Thoses lines create lists of hits per user for each time slot
        logins = list(result1.keys())  
            
        hits_8_to_12 = [result1[login] for login in logins]
        hits_12_to_16 = [result2[login] for login in logins]
            
        # This line creates the figure of the histogram without showing it
        plt.subplots(figsize=(15,6))
        plt.figure(figsize=(10, 6))
            
        # This lines sets the width of the bars for each time slot
        bar_width = 0.35
            
        # Thoses lines position the bars for the two time slots
        plt.bar([i - bar_width/2 for i in range(len(logins))], hits_8_to_12, width=bar_width, alpha=0.5, label='8h-12h')
        plt.bar([i + bar_width/2 for i in range(len(logins))], hits_12_to_16, width=bar_width, alpha=0.5, label='12h-16h')
            
        plt.xlabel('Logins des élèves')
        plt.ylabel('Nombres de hits')
        plt.title('Nombres de « hits » séparés en 2 blocs de 4 heures pour chaque élève du groupe')
        plt.legend()
            
        # Thoses lines are to put the logins on the x axis of the histogram
        plt.xticks(range(len(logins)), logins, rotation=45, ha='right')
        plt.tight_layout()
            
        # Those lines are to save the histogram in a file
        save_path = './www/medias/GraphLane.png'
        plt.savefig(save_path)
          
    except Exception as e: # The lines indented to this one will work if any error is found
        print(f"Error diagrammeLane : {str(e)}") # This line displays an error message 