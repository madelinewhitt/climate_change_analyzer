import pandas as pd
import os
#This file uses NaturalDisasters1900-2025WithCoords.csv data and 
#reduces the data used by the machine learning algorithm


inputFilePath = "../data/NaturalDisasters1900-2025WithCoords.csv"

outputFilePath = "../data/NaturalDisastersOnly.csv"

df = pd.read_csv(inputFilePath)


#1) Only keeping natural disasters 

naturalDisastersOnly = df[df["Disaster Group"]== "Natural"]

naturalDisastersOnly.to_csv(outputFilePath, index=False)


#2) Separating rows by Disaster Types

ofp = pd.read_csv(outputFilePath)


earthquakesOnlyFP = "../data/earthquakesOnlyFP.csv"
earthquakesOnly = ofp[ofp["Disaster Type"]=="Earthquake"]

earthquakesOnly.to_csv(earthquakesOnlyFP, index=False)








