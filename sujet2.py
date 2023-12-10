def mainsujet2(path: str ="./opendata/trace.csv", login: list= []) -> None: 
    """This function will give, for each member of the group, the number of « hits »
    for « Games » and « Gambling » between 8AM and 4PM"""
    #________________________________________________________________________________________
    login = ["soleilhb", "rouxfab", "lanel", "hauespl"] #Variable
    result = {noslogin: 0 for noslogin in login}        #Initialization
    #________________________________________________________________________________________
    import csv #This line is to import the csv library   
    try : #Is bassicaly an error tester
        with open(path, newline='\n',encoding='utf-8') as csvFile : #Is a csv reader
            data = csv.reader(csvFile,delimiter=';') #This line is to delimit the csv file
            next(data) #This line is to skip the first line in the csv file
            for line in data : #The indented commands linked to this one will work for each line in the file
             c = line[5] #The [c] variable takes the sixth column as a string value
             hits = line[8] #The [hits] variable takes the ninth column as a string value
             t = ((line[0]).split(" "))[1] #The [t] variable takes the time in the first column as a string value
             names = ((line[2]).split("@")[0]) #The [names] variable takes the names in the third column as a string value
             if c == "Gambling" or c =="Games" and int(t[0:2]) >= 8 and int(t[0:2]) <= 16 : #Makes the needed researches in the first and sixth column
                if names in login : #The indented command will work if the value of the [names] variable corresponds to one of the values in the [login] variable
                    result[names] += int(hits) 
            print (result) # Prints the result (The value of the [result] variable in this case)
    except FileNotFoundError as e : #The indented command will work if a FileNotFoundError is detected
        print(f"'{path}' doesn't exist") #Prints a preset error message
    except PermissionError as e : #The indented commands will work if a PermissionError is detected
        print(f"You don't have the permissions on '{path}'") #Prints a preset error message
    