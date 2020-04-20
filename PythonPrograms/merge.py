import pandas as pd
import numpy as np

sourceDF = pd.read_excel('merge.xlsx',sheet_name='sourceINSGrid')
sourceDF = pd.DataFrame(sourceDF,columns = ['grid','MatchStatusCode','sourcecode'] )
print(sourceDF)

grid = sourceDF['grid'].values.tolist()
print(grid)
MatchStatusCodevalues = sourceDF['MatchStatusCode'].values.tolist()
print(MatchStatusCodevalues)
sourcecodevalues = sourceDF['sourcecode'].values.tolist()
print(sourcecodevalues)

d1 = {'GRID':grid,
      'MatchStatusCode':MatchStatusCodevalues,
      'sourcecode':sourcecodevalues}
d1 = pd.DataFrame(d1)
print("minimum")
print(d1[["MatchStatusCode","sourcecode"]].max(axis=1))
#print(d1.groupby("GRID")[["MatchStatusCode","sourcecode"]].max(axis=1))
#sourceDF["maxvalue"] = d1[["MatchStatusCode","sourcecode"]].max(axis=1)
d1["maxvalue"] = d1[["MatchStatusCode","sourcecode"]].max(axis=1)
print(d1)
print(d1.groupby("GRID")[["maxvalue"]].max(axis=1))












# ead_excel('merge.xlsx',sheet_name='sourceINSGrid')
#sourceDF = pd.DataFrame(sourceDF,columns = ['grid', 'sourcecode','mdmid', 'FirstNameStandardized', 'LastNameStandardized','MiddleName', 'FormerLastName'])
#sourceDF = pd.DataFrame(sourceDF,columns = ['mdmid'] ,index = [1])
#sourceDF = pd.DataFrame(sourceDF)
#sourceDF = sourceDF[sourceDF['sourcecode']=='INS']
#print(sourceDF.columns)
#print(sourceDF.groupby(pd.Grouper(key = sourceDF['grid'])[sourceDF['SourceCreatedDate']].min()))
#print(pd.Grouper(key='grid'))
#sourceDF = pd.DataFrame(pd.Grouper(key='grid'))
#sourceDF.groupby(pd.Grouper(key='grid')['SourceCreatedDate','SourceLastUpdatedDate','SourceDBLastUpdate']).agg()
#sourceDF = sourceDF.fillna(0)

#sourceDF[sourceDF['SourceCreatedDate']].max(axis=0)
#SourceCreatedDate =  sourceDF.groupby("grid").apply(lambda df:df.irow(df.value.argmax()))

#sourceDF1 = sourceDF[sourceDF['SourceCreatedDate'],sourceDF['SourceLastUpdatedDate']].min(axis=1)
#print(sourceDF[sourceDF.index.duplicated()])
#sourceDF = sourceDF [sourceDF['grid']==4351919]
#sourceDF =  sourceDF.groupby((sourceDF['grid'])[sourceDF['sourcecode']]).min()

#print(sourceDF)
#['SourceCreatedDate','SourceLastUpdatedDate','SourceDBLastUpdate'].sum())
#sourceDF = sourceDF.groupby('grid').max()
#print(sourceDF['FirstNameStandardized'])
#targetDF = pd.read_excel('merge.xlsx',sheet_name='TargetINSGrid')
#targetDF = pd.DataFrame(targetDF,columns=['grid','FirstNameStandardized', 'LastNameStandardized','MiddleName', 'FormerLastName'])
#print(targetDF)
#print(targetDF['FirstNameStandardized'])


#d = {'Name':['Priya','Anusha'],
 #    'Age':[10,30],
  #   'Score':[34,56]}

#d = pd.DataFrame(d)
#print(d)

#print(d[["Age","Score"]].max(axis=1))








