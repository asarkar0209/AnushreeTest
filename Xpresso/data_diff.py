import pandas as pd



DF1='/home/abzooba/PycharmProjects/AnushreeTest/Xpresso/datasets/dataset1.csv'
# DF2='/home/abzooba/PycharmProjects/AnushreeTest/Xpresso/datasets/dataset2.csv'
DF2='/home/abzooba/PycharmProjects/AnushreeTest/Xpresso/datasets/dataset3.csv'

df1 = pd.read_csv(DF1)
df2 = pd.read_csv(DF2)

dfs_dictionary = {'DF1':df1,'DF2':df2}
df=pd.concat(dfs_dictionary)
print(df.drop_duplicates(keep=False))



# https://stackoverflow.com/questions/20225110/comparing-two-dataframes-and-getting-the-differences
# https://pythondata.com/quick-tip-comparing-two-pandas-dataframes-and-getting-the-differences/
