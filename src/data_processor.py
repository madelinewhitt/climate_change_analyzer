import pandas as pd

def getData(file_name):
    df = pd.read_csv(file_name, encoding='ISO-8859-1')

    print(checkCoords(df))
    # print(df.columns)
    # count = 0
    # for col in df.columns:
    #     count +=1
    #     print(str(count) + " " + col)

def checkCoords(df):
    pairCount = 0
    onlyLong = 0
    onlyLat = 0
    nothing = 0
    #26918 entries
    #Longitude 24
    #Latitude 23
    #we expect len(df)
    for item in df.iterrows():
        # print(row[1]['Latitude'])
        row = item[1]
        lonExist = row['Longitude'] > 0
        latExist = row['Latitude'] > 0
        if lonExist and latExist:
            pairCount += 1
        elif lonExist:
            onlyLong += 1
        elif latExist:
            onlyLat += 1        
        else:
            nothing += 1
    pairs = ("Pairs:",pairCount)
    longs = ("Only Long",onlyLong)
    lats = ("Only Lat",onlyLat) 
    none = ("Nothing", nothing)
    return(pairs,longs,lats,none)




if __name__ == "__main__":
    #anything that is not a function will be here
    file_name = "../data/NaturalDisasters1900-2025.csv"

    getData(file_name)
