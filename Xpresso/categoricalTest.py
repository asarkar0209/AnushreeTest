import statistics as s
import pandas as pd
import numpy as np
from numpy import ndarray
from scipy import stats
from scipy.stats import chi2_contingency
from scipy.stats import chi2

df = pd.read_csv("datasets/test_case1.csv")

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
        print('')
        print('\n')

datacrossed=pd.crosstab(df['Gender'],df['Happiness'],margins = False)
print(datacrossed)
print('')

stat, p, dof, expected = chi2_contingency(datacrossed)
# print(stat)
# print(p)
# print(dof)
# print(expected)

'''A probability of 95% can be used, 
suggesting that the finding of the test is quite likely given the assumption of the test that the variable is independent.
If the statistic is less than or equal to the critical value, we can fail to reject this assumption, otherwise it can be rejected.'''
prob = 0.95
critical = chi2.ppf(prob, dof)
if abs(stat) >= critical:
	print('Dependent (reject H0)')
else:
	print('Independent (fail to reject H0)')

'''We can also interpret the p-value by comparing it to a chosen significance level,
 which would be 5%, calculated by inverting the 95% probability used in the critical value interpretation.'''

alpha = 1.0 - prob
if p <= alpha:
	print('Dependent (reject H0)')
else:
	print('Independent (fail to reject H0)')



