import statistics as s
import pandas as pd
import numpy as np
from numpy import ndarray
from scipy import stats

df = pd.read_csv("test_case1.csv")

print('Welcome to the Categorical QA Test!')
print("||'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''||")
print(df.info())

for col in df.columns:
    # print('\n', pd.Categorical(df[col]))
    print("********************************************************")
    print(df[col].describe())
    if df[col].dtype=='int64' or df[col].dtype=='float64':
        print("Median :: ",s.median(df[col])," , ", end=' ')
        # print(s.mode(df[col]), " , ", end=' ')
        print("Variance :: ", s.variance(df[col]), " , ", end=' ')
        print("pVariance :: ", s.stdev(df[col]), " , ", end=' ')