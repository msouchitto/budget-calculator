import json

def fileRW():
    readStream = open("data.txt")

    #first line/value is income per week
    _income = int(readStream.readline())
    print("Weekly Income: ", _income);
    print("Monthly Income: :", _income * 4)

    readStream.close()
    
    #write income to file
    fileStream = open("data.txt", "w")
    fileStream.write(str(_income))

    fileStream.close()

def readFromFile():
    readStream = open("data.txt")
    x = readStream.read()
    #first line/value is income per week
    _income = json.loads(x)

    #mike = '{ "income" : 576, \"monthlyRent\" : 750 }'
    #print(y["mike"]["income"])

    return _income["mike"]["income"];
