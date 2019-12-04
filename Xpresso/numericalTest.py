import numpy as np
import pandas as pd
import statistics as s
from scipy.stats import iqr
import scipy.special as scsp



print("Welcome to the first QA Test!")
print("\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")

class Explorer():
#Description of the Data
    def __init__(self,data):
        self.data=pd.read_csv(data_path)
        self.numericAnalysis()
        self.correlationCalculation()

#Lets start with the Numerical Analysis
    def numericAnalysis(self):
        print("**********************************************************************************")
        print(list(self.data))
        print("Median:: ", end='')
        for col in self.data.columns:
            if self.data[col].dtype=='int64' or self.data[col].dtype=='float64':
                print(s.median(self.data[col]),", ", end='')
        print("")
        print("Mode:: ", end='')
        for col in self.data.columns:
            if self.data[col].dtype=='int64' or self.data[col].dtypes=='float64':
                print(s.mode(self.data[col]),", ", end='')

        print("")
        print("Variance:: ", end='')
        for col in self.data.columns:
            if self.data[col].dtype == 'int64' or self.data[col].dtypes=='float64':
                print(s.variance(self.data[col]),", ", end='')

        print("")
        print("P-variance:: ", end='')
        for col in self.data.columns:
            if self.data[col].dtype=='int64' or self.data[col].dtypes=='float64':
                print(s.variance(self.data[col],s.mean(self.data[col])),", ", end='')

        print("")
        print("Standard Deviation:: ", end='')
        for col in self.data.columns:
            if self.data[col].dtype=='int64' or self.data[col].dtypes=='float64':
                print(s.stdev(self.data[col]),", ", end='')

        print("")
        print("Inter Quartile Ratio:: ", end='')
        for col in self.data.columns:
            if self.data[col].dtype == 'int64' or self.data[col].dtypes == 'float64':
                print(iqr(self.data[col])," , ",end='')

        print("")
        print('<<<--------------------------------------------------------------------------------------------------------------->>>')
        print("Deciles:: It sort data into ten equal parts: The 10th, 20th, 30th, 40th, 50th, 60th, 70th, 80th, 90th and 100th percentiles. \n", end='')
        print('<<<--------------------------------------------------------------------------------------------------------------->>>')
        for col in self.data.columns:
            if self.data[col].dtype=='int64' or self.data[col].dtypes=='float64':
                print("For:",col)
                print("\n", pd.qcut(self.data[col], 10, labels=None, retbins=False, precision=3, duplicates='drop'))
                print('********************************************************************************************')
        print('')
        print('<<<--------------------------------------------------------------------------------------------------------------->>>')
        print("Quartiles:: The values that split the data into fourths are the quartiles. \n", end='')
        print('<<<--------------------------------------------------------------------------------------------------------------->>>')
        for col in self.data.columns:
            if self.data[col].dtype=='int64' or self.data[col].dtypes=='float64':
                print("\n", pd.qcut(self.data[col], 4, labels=None, retbins=False, precision=3, duplicates='drop'))
                print('********************************************************************************************')

        print('<<<--------------------------------------------------------------------------------------------------------------->>>')
        print('Skewness:\n',self.data.skew())
        print('<<<--------------------------------------------------------------------------------------------------------------->>>')
        print('Kurtosis:\n',self.data.kurtosis())
        print('<<<--------------------------------------------------------------------------------------------------------------->>>')


    def correlationCalculation(self):
        print('***************************************************************************')
        pearson_data = self.data.corr(method='pearson')
        print("Correlation(Method = Pearson)")
        print(pearson_data)

        print('***************************************************************************')

        spearman_data = self.data.corr(method='spearman')
        print("Correlation(Method = Spearman)")
        print(spearman_data)

        print('***************************************************************************')

        def z_score(df):
            df.columns = [x + "_zscore" for x in df.columns.tolist()]
            return ((df - df.mean()) / df.std(ddof=0))

        print('***************************************************************************')
        z_score_data = z_score(self.data)
        print(z_score_data)
        print('***************************************************************************')

        def p_values(z_score_data):
            z_score_data.columns = [x + "_pvalues" for x in z_score_data.columns.tolist()]
            return 0.5 * (1 + scsp.erf(z_score_data / np.sqrt(2)))

        pval = p_values(z_score_data)
        print(pval)
        print('***************************************************************************')



if __name__ == "__main__":
    data_path = "/home/abzooba/PycharmProjects/xpresso.ai/datasets/haberman.csv"
    Explorer(data_path)

