import pandas as pd

file_name = "../data/naturalDisaster2000-2024(EM-DAT Data).csv"

df = pd.read_csv(file_name, encoding='ISO-8859-1')
# print(df.info())
count = 0
for d in df['Disaster Type']:
    if d=='Flood':
        count += 1
print(count)
