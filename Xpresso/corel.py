import statistics as s
import pandas as pd
import numpy as np
from scipy.stats import norm
import scipy.special as scsp

def correlationCalculation(data_path):

    df = pd.read_csv(data_path)
    print('***************************************************************************')
    pearson_data=df.corr(method ='pearson')
    print("Correlation(Method = Pearson)")
    print(pearson_data)

    print('***************************************************************************')

    spearman_data=df.corr(method ='spearman')
    print("Correlation(Method = Spearman)")
    print(spearman_data)

    print('***************************************************************************')

    def z_score(df):
       df.columns = [x + "_zscore" for x in df.columns.tolist()]
       return ((df - df.mean())/df.std(ddof=0))

    print('***************************************************************************')
    z_score_data=z_score(df)
    print(z_score_data)
    print('***************************************************************************')
    def p_values(z_score_data):
       z_score_data.columns = [x + "_pvalues" for x in z_score_data.columns.tolist()]
       return 0.5 * (1 + scsp.erf(z_score_data / np.sqrt(2)))

    pval=p_values(z_score_data)
    print(pval)
    print('***************************************************************************')





# threshold_Pval=.2
# shape = normdata.shape
# print('***************************************************************************')
# print("Null Hypothesis Test","-->",'1-->Yes','','0-->No')
# print('*******************')
# for x in range(0, shape[0]):
#     for y in range(0, shape[1]):
#         if normdata[x, y] >= threshold_Pval:
#             normdata[x, y] = 1
#         else:
#            normdata[x,y]=0
#
# print(normdata)