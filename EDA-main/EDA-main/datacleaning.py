import numpy as np 
import pandas as pd 
import seaborn as sns
import os

missing_values=["N/a","na",np.nan]
df = pd.read_csv("input.csv", na_values= missing_values)
df.isnull().sum()