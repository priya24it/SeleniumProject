import pandas as pd
import numpy as np

sourceDF = pd.read_excel('merge.xlsx',sheet_name='sourceINSGrid')
sourceDF = pd.DataFrame(sourceDF)
TotalColumns = list(sourceDF.shape)
d = {}
print(sourceDF.columns)
listofcolumns = sourceDF.columns.values.tolist()
for i in range(0,TotalColumns[1]):
    d[listofcolumns[i]] = sourceDF[listofcolumns[i]].values.tolist()

#print(d)

d = pd.DataFrame(d)
d = d.fillna(0)
print(d)

d["maxdate"] = d[["SourceCreatedDate","SourceLastUpdatedDate","SourceDBLastUpdate"]].max(axis=1)
print(d.groupby("grid")[["maxdate"]].max(axis=1))
#print(d)


Firstname = pd.DataFrame(d.copy(),columns=['grid','sourcecode','FirstName','maxdate'])
#print(Firstname)
Firstname= Firstname[Firstname['sourcecode']=='INS']
#print(Firstname)
Firstname = Firstname.drop_duplicates(subset=['grid','FirstName','maxdate'])
#print(Firstname)














