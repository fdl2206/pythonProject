import pandas as pd
csvFile = pd.read_csv("insurance.csv")

addColumn = csvFile['discount'] = csvFile['charges']*0.05

print("Hasil Filter: '\n'", csvFile.head())