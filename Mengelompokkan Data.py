import pandas as pd
csvFile = pd.read_csv("insurance.csv")

GroupingFile = csvFile.groupby('sex').agg(average_age = ('age', 'mean'), median_charges = ('charges', 'median'))

print("Hasil Grouping: '\n'", GroupingFile.head())