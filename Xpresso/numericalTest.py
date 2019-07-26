import numpy as np
from numpy import ndarray
import pandas as pd
import statistics as s
from scipy.stats import iqr


print("Welcome to the first QA Test!")
print("\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
dataset=pd.read_csv("haberman.csv")
#Description of the Data
print(dataset.describe())

#Soting the means of each column in an array
index=len(dataset.columns)
arr= ndarray(index, int)
for i in range(0,index):
    arr[i]= s.mean(dataset[list(dataset.columns)[i]])


#Lets start with the Numerical Analysis
print("**********************************************************************************")
print(list(dataset))
print("Median:: ", end='')
for col in dataset.columns:
    if dataset[col].dtype=='int64' or dataset[col].dtype=='float64':
        print(s.median(dataset[col]),", ", end='')
print("")
print("Mode:: ", end='')
for col in dataset.columns:
    if dataset[col].dtype=='int64' or dataset[col].dtypes=='float64':
        print(s.mode(dataset[col]),", ", end='')

print("")
print("Variance:: ", end='')
for col in dataset.columns:
    if dataset[col].dtype=='int64' or dataset[col].dtypes=='float64':
        print(s.variance(dataset[col]),", ", end='')

print("")
print("P-variance:: ", end='')
for col in dataset.columns:
    if dataset[col].dtype=='int64' or dataset[col].dtypes=='float64':
        print(s.variance(dataset[col],arr[i]),", ", end='')

print("")
print("Standar Deviation:: ", end='')
for col in dataset.columns:
    if dataset[col].dtype=='int64' or dataset[col].dtypes=='float64':
        print(s.stdev(dataset[col]),", ", end='')

print("")
print("Inter Quartile Ratio:: ", end='')
for col in dataset.columns:
    if dataset[col].dtype == 'int64' or dataset[col].dtypes == 'float64':
        print(iqr(dataset[col])," , ",end='')

print("")
print('<<<--------------------------------------------------------------------------------------------------------------->>>')
print("Deciles:: It sort data into ten equal parts: The 10th, 20th, 30th, 40th, 50th, 60th, 70th, 80th, 90th and 100th percentiles. \n", end='')
print('<<<--------------------------------------------------------------------------------------------------------------->>>')
for col in dataset.columns:
    if dataset[col].dtype=='int64' or dataset[col].dtypes=='float64':
        print("For:",col)
        print("\n", pd.qcut(dataset[col], 10, labels=None, retbins=False, precision=3, duplicates='drop'))
        print('********************************************************************************************')
print('')
print('<<<--------------------------------------------------------------------------------------------------------------->>>')
print("Quartiles:: The values that split the data into fourths are the quartiles. \n", end='')
print('<<<--------------------------------------------------------------------------------------------------------------->>>')
for col in dataset.columns:
    if dataset[col].dtype=='int64' or dataset[col].dtypes=='float64':
        print("\n", pd.qcut(dataset[col], 4, labels=None, retbins=False, precision=3, duplicates='drop'))
        print('********************************************************************************************')

print('<<<--------------------------------------------------------------------------------------------------------------->>>')
print('Skewness:\n',dataset.skew())
print('<<<--------------------------------------------------------------------------------------------------------------->>>')
print('Kurtosis:\n',dataset.kurtosis())
print('<<<--------------------------------------------------------------------------------------------------------------->>>')

