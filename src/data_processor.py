import pandas as pd

file_name = "../data/NaturalDisasters1900-2025.csv"

def getData():
    df = pd.read_csv(file_name, encoding='ISO-8859-1')
    print(df)
    for d in df['Disaster Type']:
        pass

if __name__ == "__main__":
    #anything that is not a function will be here
    getData()
