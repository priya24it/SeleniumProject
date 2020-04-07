import pandas as pd

dataframe = pd.read_excel("testcase.xlsx")
dataframe = pd.DataFrame(dataframe)
#print(dataframe)
#str = (dataframe.apply(lambda row:str(row["a"])+""+str(row["b"])+""+str(row["c"])+""+str(row["d"])+""+row["e"]+""+str(row["f"])+""+str(row["g"])+""+str(row["h"])+""+str(row["i"])+""+str(row["j"]) , axis = 1))
excelwriter = pd.ExcelWriter("sample.xlsx")

dataframe2 = pd.DataFrame()
dataframe2["Req"] = "1"
dataframe2["Transformation"] = "TC_duplicateCheck_" + dataframe["e"]
dataframe2["Description"] = "TC_Verify whether the transformation logic has applied as per the requirement document for the_ " + dataframe["e"]
dataframe2["Step#"] = "1"
dataframe2["Step Description"] = str
dataframe2["Expected Result"] = "Data should be loaded as per the logic"
dataframe2["Actual Result"] = dataframe["e"] + "  value should match between the source and Target logic"
dataframe2["Pass/Fail"] = ""
dataframe2["Comments"] = ""
dataframe2["Created By"] = ""
dataframe2["Executed By"] = ""
dataframe2["Created Date"] = ""
dataframe2.to_excel(excelwriter,sheet_name="s2")

str = (dataframe.apply(lambda row:str(row["a"])+" "+str(row["b"])+" "+str(row["c"])+" "+str(row["d"])+" "+str(row["e"])+" "+str(row["f"])+""+str(row["g"]) , axis = 1))
print(len(str))
dataframe["combined"] = str
dataframe["Req"] = "1"
dataframe["Transformation"] = "TC_TransformationCheck_" + dataframe["e"]
dataframe["Description"] = "TC_Verify whether the transformation logic has applied as per the requirement document for the_ " + dataframe["e"]
dataframe["Step#"] = "1"
dataframe["Step Description"] = str
dataframe["Expected Result"] = "Data should be loaded as per the logic"
dataframe["Actual Result"] = dataframe["e"] + "  value should match between the source and Target logic"
dataframe["Pass/Fail"] = ""
dataframe["Comments"] = ""
dataframe["Created By"] = ""
dataframe["Executed By"] = ""
dataframe["Created Date"] = ""

print(dataframe["combined"])


dataframe1 = pd.DataFrame()
dataframe1["Req"] = dataframe["Req"]
dataframe1["Test Case#"] = dataframe["Transformation"]
dataframe1["Description"] = dataframe["Description"]
dataframe1["Step#"]  =dataframe["Step#"]
dataframe1["Step Description"] = dataframe["Step Description"]
dataframe1["Expected Result"]  =dataframe["Expected Result"]
dataframe1["Actual Result"] =dataframe["Actual Result"]
dataframe1["Pass/Fail"] =dataframe["Pass/Fail"]
dataframe1["Comments"] =dataframe["Comments"]
dataframe1["Created By"] =dataframe["Created By"]
dataframe1["Executed By"] =dataframe["Executed By"]
dataframe1["Created Date"] =dataframe["Created Date"]

#dataframe1.to_excel("sample.xlsx")
dataframe1.to_excel(excelwriter,sheet_name="s1")
excelwriter.save()

