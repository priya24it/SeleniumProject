import pandas as pd


l1 = ['map.contact_main','Sheet1','map.contact_main_multiple','map.contact_phone']
writer = pd.ExcelWriter("sample.xlsx")
sheetname = "map.contact_main"
dataframe = pd.read_excel("testcase.xlsx")
dataframe = pd.DataFrame(dataframe)

for i in range(0,len(l1)):
    dataframe = pd.read_excel("testcase.xlsx",sheet_name=l1[i])
    dataframe = pd.DataFrame(dataframe)
    print(l1[i])
    print(dataframe.head(4))

    str = (dataframe.apply(lambda row: row["a"], axis=1))

    Dict1 = {}
    Dict1["Req"] = ['1']
    Dict1["Transformation"] = ['TC_countvalidation']
    Dict1["Description"] = ['TC_Verification of count between the source and target table']
    Dict1["Step#"] = ['1']
    Dict1["Step Description"] = ['']
    Dict1["Expected Result"] = ['select mdmid,count(*) from map.contact_main where 1=1 group by mdmid having count(*) > 1 ']
    Dict1["Actual Result"] = [' Duplicates should not exists on the latest processID. We should have all unique records ']
    Dict1["Pass/Fail"] = ['']
    Dict1["Comments"] = ['']
    Dict1["Created By"] = ['']
    Dict1["Executed By"] = ['']
    Dict1["Created Date"] = ['']
    dataframe3 = pd.DataFrame(Dict1)
    print(dataframe3)


    DupDict = {}
    DupDict["Req"] = ['1']
    DupDict["Transformation"] = ['TC_duplicateCheck_MDMID']
    DupDict["Description"] = ['Check whether there are any duplicates in the data loaded on the latest processID']
    DupDict["Step#"] = ['']
    DupDict["Step Description"] = ['Verify the count of the source table using below query in the MDM database select count(*) from crm.s_contact where change_flag= Y , Verify the count of the target table using below query in the MDM database b select count(*) from map.contact_main  where 1=1 Note: Please apply processID filter for both the tables Verify the count between the  source and target table. ']
    DupDict["Expected Result"] = ['select mdmid,count(*) from map.contact_main where 1=1 group by mdmid having count(*) > 1 ']
    DupDict["Actual Result"] = [' Duplicates should not exists on the latest processID. We should have all unique records ']
    DupDict["Pass/Fail"] = ['']
    DupDict["Comments"] = ['']
    DupDict["Created By"] = ['']
    DupDict["Executed By"] = ['']
    DupDict["Created Date"] = ['']
    dataframe1 = pd.DataFrame(DupDict)
    print(dataframe1)


    dataframe2 = pd.DataFrame()
   # str = (dataframe.apply(lambda row: row["a"],axis = 1))
    str = (dataframe.apply(lambda row:row["a"]+" "+row["b"]+" "+row["c"]+" "+row["d"]+" "+row["e"]+" "+row["f"]+""+row["g"] , axis = 1))
    #str = ''
    print(len(str))
    dataframe2["Req"] = "1"
    dataframe2["Transformation"] = "TC_TransformationCheck_" + dataframe["e"]
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

    df = pd.concat([dataframe3,dataframe1, dataframe2])
    df.to_excel(writer,l1[i])
    print(df)


    workbook=writer.book
    worksheet = writer.sheets[l1[i]]

    format = workbook.add_format({'text_wrap': True})
    # Setting the format but not setting the column width.
    worksheet.set_column('C:C', 15, format)
    worksheet.set_column('D:D', 15, format)
    worksheet.set_column('B:B', 15, format)
    worksheet.set_column('F:F', 15, format)
    worksheet.set_column('G:G', 15, format)
    worksheet.set_column('H:H', 15, format)
    worksheet.set_column('E:E', 15, format)
    worksheet.set_column('A:A', 15, format)

writer.save()
