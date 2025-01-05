import pandas as pd
csvFile = pd.read_csv("insurance.csv")
dfSort = csvFile.sort_values(by=['sex'])
dfDesc = csvFile.sort_values(by=['sex'], ascending=False)

print("Hasil Sorting Ascending: '\n'", dfSort.head())
print("Hasil Sorting Descending: '\n'", dfDesc.head())