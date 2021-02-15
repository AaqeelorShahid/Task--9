import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

df = pd.read_csv("AirQuality.csv")
num_records = len(df)
print (num_records)

df.isnull().values.any()

df.isnull().sum()

records = []
for i in range(0, num_records):
    records.append([str(df.values[i,j]) for j in range(0, 8)])
    
association_rules = apriori(records, min_support=0.0100, min_confidence=0.4, min_lift=3, min_length=3)
association_results = list(association_rules)


for item in association_results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")