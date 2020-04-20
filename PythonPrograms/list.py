import pytest
import pandas as pd

#dataframe = pd.read_excel("testdata.xlsx")
#dataframe = pd.DataFrame(dataframe)
#dict = dataframe.values.tolist()
#print(dict)
#dict = str(dict)
#print("string value" + dict)
#i = len(dict)
#print("length of the string" + str(i))
#dict= "priya"
#dict = dict[1:5-1]
#dict = dict.replace("[","(")
#dict = dict.replace("]",")")
#print(dict)

#dict = "[" + dict + "]"
#print(dict)
#print(len(dict))
SampleExcel = pd.read_excel("sample.xlsx")
df = pd.DataFrame(SampleExcel)
print(df['Step#'].value_counts())
df = pd.DataFrame(df['Step#'].value_counts()>1).reset_index().rename(columns={"Step#": "grid", "index": "NoofTimes"})
print(df)
df = df[df['NoofTimes']==True]
print(df)


dict1 = {"StdudentName":['Priya','Ashok'],
         "Age":[2,3]}

print(dict1.values())






