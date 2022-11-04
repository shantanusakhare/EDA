import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport
def load_csv():
    csv= pd.read_csv('OnePieceArcs.csv')
    return csv
df = load_csv()
pr = ProfileReport(df, explorative=True)
pr.to_file("output.html")