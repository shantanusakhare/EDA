import numpy as np 
import pandas as pd
import seaborn as sns
import os

missing_value = ["N/a","na",np.nan]
df = pd.read_csv("Book1.csv",na_values=missing_value)
print(df)
# sns.heatmap(df.isnull(),yticklabels=False, annot=True)
# print(df.isnull().sum())
# print(df.dropna(how="all"))
# print(df.fillna(0))
# print(df.fillna(method = 'ffill'))
# meeen= df.iloc[:,0:3].apply(np.mean)
for x in range( len(df.columns)):
    for y in range(len(df.rows)):
        list=[]
        if(pd.isnull()):
            print(df.iloc[:len(df)])

# for index, row in df.iterrows():
#     if(pd.isnull(row['myCol'])):
#             print('true')

# print(df['sept'].mean())
# print(df.apply(np.min))