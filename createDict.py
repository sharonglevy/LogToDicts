import re

listDicts = []

def main():
    #open and read line by line of the file
    with open("test.log", "r") as file:
        for line in file:
            #Extract the info from the line
            date = line.split(' ', 1)[0]
            #If Dmer
            try:
                typeP = re.search(r'] (.*?) DMErr', line).group(1)
                dmerr = dmer(line, typeP)
                switch = "d"
            #If intErr
            except:
                typeP = re.search(r'] (.*?) IntErr', line).group(1)
                inter = interr(line, typeP)
                switch = "i"
            finally:
                #contruction of the dicts
                dct = {"date": date,
                    "type": typeP}
                #If it was Dmer
                if switch == "d":
                    for part in dmerr:
                        part1 = part.split("=")[0]
                        part2 = part.split("=")[1]
                        dct[part1] = part2
                #If it was intErr
                else:
                    #for each part of the list that we extracted
                    for part in inter:
                        #replace first = of the second half  with : to then convert to dict key and values
                        part = part.replace("=", ":", 1)
                        part1 = part.split(":")[0]
                        part2 = part.split(":")[1]
                        dct[part1] = part2
                #append the new dict to the list of dictionaries
                listDicts.append(dct)
        #print the list of dictionaries to the console
        for dict in listDicts:
            print(dict)
    return True


def dmer (line, typeP):
    #get the second half to work with
    secDict = line.split(typeP, 1)[1]
    #split it by spaces into a list
    secDict = secDict.split()
    return secDict


def interr(line, typeP):
    #second half
    secDict = line.split(typeP, 1)[1]
    #split it by ; (if it has) into a list
    secDict = secDict.split(";")
    secDict = list(secDict)
    return secDict

if __name__ == "__main__":
    main()