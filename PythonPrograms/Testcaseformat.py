import pandas as pd

sheetname = "map.contact_main"
dataframe = pd.read_excel("testcase.xlsx")
dataframe = pd.DataFrame(dataframe)

Dict1 = {}
Dict1["Req"] = ['1']
Dict1["Transformation"] = ['TC_countvalidation_map.Contact_main']
Dict1["Description"] = ['TC_Verification of count between the source and target table']
Dict1["Step#"] = ['1']
Dict1["Step Description"] = ['hh']
Dict1["Expected Result"] = ['select mdmid,count(*) from map.contact_main where 1=1 group by mdmid having count(*) > 1 ']
Dict1["Actual Result"] = ['Duplicates should not exists on the latest processID. We should have all unique records ']
Dict1["Pass/Fail"] = ['']
Dict1["Comments"] = ['']
Dict1["Created By"] = ['']
Dict1["Executed By"] = ['']
Dict1["Created Date"] =['']
df1 = pd.DataFrame(Dict1)
print(df1)
df1.to_excel("sample.xlsx")
