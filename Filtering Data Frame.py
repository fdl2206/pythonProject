import pandas as pd
csvFile = pd.read_csv("insurance.csv")
dfFilter =csvFile.filter(items=['sex', 'region'])

print("Hasil Filter: '\n'", dfFilter.head())