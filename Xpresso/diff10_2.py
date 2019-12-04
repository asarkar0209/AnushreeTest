import pandas as pd

df_1 =  pd.read_csv('/home/abzooba/PycharmProjects/AnushreeTest/Xpresso/datasets/dataset4.csv')
print(df_1)
print('*********************************************')
df_2 =  pd.read_csv('/home/abzooba/PycharmProjects/AnushreeTest/Xpresso/datasets/dataset2.csv')
print(df_2)
print('*********************************************')
print('Common in two dataframes')
print(df_1[df_1.columns.intersection(df_2.columns)])
print('*********************************************')
print('Column(s) in df_1 but not in df_2')
cols_removed=df_1[df_1.columns.difference(df_2.columns)]
print(cols_removed)
print('*********************************************')
print('Column(s) in df_2 but not in df_1')
cols_added=df_2[df_2.columns.difference(df_1.columns)]
print(cols_added)
print('*********************************************')

def count_cols_added():
    count=0
    list2=[]
    for cols in cols_added.columns:
        count=count+1
        list2.append(cols)
    print(list2)
    print('Columns added in df_2 = ',count)

count_cols_added()
print('------------------------------------------------------')

def count_cols_removed():
    count=0
    list2=[]
    for cols in cols_removed.columns:
        count=count+1
        list2.append(cols)
    print(list2)
    print('Columns removed from df_2 = ',count)

count_cols_removed()
print('------------------------------------------------------')

print('******************************************************************')
print('Row count difference')
print(df_2[ ~df_2.isin(df_1)].dropna())


