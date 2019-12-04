import pandas as pd


df1=pd.DataFrame([
    {'Date': '2013-11-24', 'Fruit': 'Banana','Num': 22.1,'Color': 'Yellow','Country':'India'},
    {'Date': '2013-11-24', 'Fruit': 'Orange','Num':  8.6,'Color': 'Orange','Country':'Russia'},
    {'Date': '2013-11-24', 'Fruit': 'Apple','Num': 7.6,'Color': 'Green','Country':'Kenya'},
    {'Date': '2013-11-24', 'Fruit': 'Celery','Num': 10.2,'Color': 'Green','Country':'Ireland'},
    {'Date': '2013-11-24', 'Fruit': 'Banana','Num': 15.2,'Color': 'Green','Country':'Poland'}
])

print(df1)


df2=pd.DataFrame([
    {'Date': '2013-11-24', 'Fruit': 'Banana','Num': 22.1,'Color': 'Yellow'},
    {'Date': '2013-11-24', 'Fruit': 'Orange','Num':  8.6,'Color': 'Orange'},
    {'Date': '2013-11-24', 'Fruit': 'Apple','Num': 7.6,'Color': 'Green'},
    {'Date': '2013-11-24', 'Fruit': 'Celery','Num': 10.2,'Color': 'Green'},
    {'Date': '2013-11-25', 'Fruit': 'Apple','Num': 22.1,'Color': 'Red'},
    {'Date': '2013-11-25', 'Fruit': 'Orange','Num': 8.6,'Color': 'Orange'}
])


# https://stackoverflow.com/questions/20225110/comparing-two-dataframes-and-getting-the-differences

print('*****************************************')
print(df2)


print('*************************************************')
# concatenate dataframes:
df = pd.concat([df1, df2])
df = df.reset_index(drop=True)

# group by
df_gpby = df.groupby(list(df.columns))
# print(df_gpby.groups.values())

print('*************************************************')

# get index of unique records
idx = [x[0] for x in df_gpby.groups.values() if len(x) == 1]
print('*************************************************')
# filter
print(df.reindex(idx))
