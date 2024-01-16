import csv  # This line imports the csv library

def mainsujet2(src: str, logins: list, change: str) -> list:
    """
    This function reads a CSV file, filters data based on specific conditions, and calculates hits
    for given logins within defined time intervals. 
    It takes two strings ('src' and 'change') and one list ('logins') as parameters and returns a list.
    It handles different cases based on the 'change' parameter ('a' or 'b') to process data and generate results accordingly.
    """
    #_________________________________________________________________
    result1 = {login: 0 for login in logins}
    result2 = {login: 0 for login in logins}  #Initialization
    result3 = {login: 0 for login in logins}
    #_________________________________________________________________

    try: # This is bassicaly an error tester. The program will work if no error is found.
        with open(src, newline='\n', encoding='utf-8') as csvFile: # This line opens the csv file
            data = csv.reader(csvFile, delimiter=';') # This line is to read the csv file
            next(data)  # This lines is to skip the header row of the csv file

            # Thoses lines extracts relevant data from the CSV file under specific conditions
            for line in data:
                category = line[5]  
                hits = line[8]      
                time = ((line[0]).split(" "))[1]  
                names = ((line[2]).split("@")[0])  
                
                if category in ["Gambling", "Games"]:
                    if names in logins:
                        match change:
                            case "a":
                                if 8 <= int(time[0:2]) < 12: 
                                    result1[names] += int(hits)
                                elif 12 <= int(time[0:2]) < 16: 
                                    result2[names] += int(hits)
                                Fresult = [result1, result2]
                            case "b": 
                                if 8 <= int(time[0:2]) < 16: 
                                    result3[names] += int(hits)
                                Fresult = result3

        return Fresult  # This line returns the calculated final result which changes depending on the case

    except Exception as e: # The lines indented to this one will work if any error is found
        print(f"Error sujet 2 : {str(e)}")  # This line displays an error message 