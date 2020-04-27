import pandas as pd

#l1 = ['map.contact_main','rel','map.contact_main_multiple','map.contact_phone','job','map.contact_board']
l1 = ['map.contact_board']
writer = pd.ExcelWriter("sample.xlsx")
sheetname = "map.contact_board"
dataframe = pd.read_excel("testcase.xlsx",sheet_name ="map.contact_board")
dataframe = pd.DataFrame(dataframe)


for i in range(0,len(l1)):
    dataframe = pd.read_excel("testcase.xlsx",sheet_name="map.contact_board")
    dataframe = pd.DataFrame(dataframe)
    print(dataframe.dtypes)
   # print(dataframe.head(4))

    str = (dataframe.apply(lambda row: row["a"], axis=1))

    Dict4 = {}
    Dict4["Req"] = ['1']
    count = "TC01_Onbaording the "+ l1[i] + "   into MDM Raw layer."
    Dict4["Transformation"] = [count]
    desc = """ Open the Microsoft SQL Server,Go to the Databases folder and expand it. 
                Go to the Tables folder right click on the """ +l1[i]+ """table a new window will open with metadata. 
                Go to the Tables folder right click on the """ +l1[i]+ """table a new window will open with metadata. 
                Verify the struture of the both the tables. """
    desc1 = "TC_Verification of structure for onbaording" + l1[i]
    Dict4["Description"] = [desc1]
    Dict4["Step#"] = ['1']
    Dict4["Step Description"] = [desc]
    Dict4["Expected Result"] = ['Structure should match between Source and Target table.']
    Dict4["Actual Result"] = ['Structure should match between Source and Target table.']
    Dict4["Pass/Fail"] = ['']
    Dict4["Comments"] = ['']
    Dict4["Created By"] = ['']
    Dict4["Executed By"] = ['']
    Dict4["Created Date"] = ['']
    dataframe4 = pd.DataFrame(Dict4)


    Dict1 = {}
    Dict1["Req"] = ['1']
    count = "TC00_Countvalidation_" + l1[i]
    Dict1["Transformation"] = [count]
    Dict1["Description"] = ['TC_Verification of count between the source and target table']
    Dict1["Step#"] = ['1']

    text = """ Verify the count of the source table using below query in the MDM Raw Layer \n select count(*) from crm.s_contact where change_flag= 'Y' \n  
                   Verify the count of the target table using below query in the MDM MAP layer \n select count(*) from """ +  l1[i] + """ \n 
                   Note: Please apply processID filter for both the tables Verify the count between the  source and target table. """

    Dict1["Step Description"] = [text]
    Dict1["Expected Result"] = ['Count should match between source and target on the latest process ID.']
    Dict1["Actual Result"] = ['Count should match between source and target on the latest process ID.']
    Dict1["Pass/Fail"] = ['']
    Dict1["Comments"] = ['']
    Dict1["Created By"] = ['']
    Dict1["Executed By"] = ['']
    Dict1["Created Date"] = ['']
    dataframe3 = pd.DataFrame(Dict1)
    #print(dataframe3)

   #Check whether there are any duplicates in the data loaded on the latest processID

    DupDict = {}
    DupDict["Req"] = ['1']
    DupDict["Transformation"] = ['TC_Verification of duplicates in the data']
    desc = 'Check whether there  any duplicates exists on the latest processID in ' + l1[i] + 'table.'
    DupDict["Description"] = [desc]
    DupDict["Step#"] = ['1']


    DupDict["Step Description"] = ['Check whether there are any duplicates in the data loaded on the latest processID']

    er = """Below Query will be used to identify the duplicates  
                select mdmid,count(*) from """ + l1[i] + """where 1=1 group by mdmid having count(*) \n
                Note: Please apply processID filter while validating the data  """

    DupDict["Expected Result"] = [er]
    DupDict["Actual Result"] = [' Duplicates should not exists on the latest processID. We should have all unique records ']
    DupDict["Pass/Fail"] = ['']
    DupDict["Comments"] = ['']
    DupDict["Created By"] = ['']
    DupDict["Executed By"] = ['']
    DupDict["Created Date"] = ['']
    dataframe1 = pd.DataFrame(DupDict)


    # k replaces bb
    dataframe2 = pd.DataFrame()
    #str = (dataframe.apply(lambda row:row["i"]+"\n"+row["a"]+" "+row["b"]+" " +row["c"]+" "+row["k"]+" "+row["l"]+" \n"+row["j"] + "  \n "+row["d"]+"  "+row["e"]+" "+row["f"]+" \n "+row["g"]+" \n "+row["h"] , axis = 1))

    str = (dataframe.apply(lambda row: row["aa"]+"\n"+row["a"]+" "+row["aa1"]+" \n "+row["d"]+"  "+row["e"]+" "+row["f"]+" \n "+row["g"]+" \n"+row["h"], axis = 1))

    #str = (dataframe.apply(lambda row: row["aa"] +  row["a"] , axis=1))
    print(str)

    dataframe2["Req"] = "1"
    dataframe2["Transformation"] = "TC_TransformationCheck_" + dataframe["e"]
    dataframe2["Description"] = "TC_Verify whether the transformation logic has applied as per the requirement document for the column  " + dataframe["e"]
    dataframe2["Step#"] = "1"
    dataframe2["Step Description"] = str
    dataframe2["Expected Result"] = "Data should be loaded as per the Transformation logic"
    dataframe2["Actual Result"] = dataframe["e"] + "  value should match between the Source and Target tables"
    dataframe2["Pass/Fail"] = ""
    dataframe2["Comments"] = ""
    dataframe2["Created By"] = ""
    dataframe2["Executed By"] = ""
    dataframe2["Created Date"] = ""

    df = pd.concat([dataframe4,dataframe3,dataframe1, dataframe2])
    df.to_excel(writer,l1[i])
    #print(df)


    workbook=writer.book
    worksheet = writer.sheets[l1[i]]

    format = workbook.add_format({'text_wrap': True})
    # Setting the format but not setting the column width.
    worksheet.set_column('C:C', 20, format)
    worksheet.set_column('D:D', 25, format)
    worksheet.set_column('B:B', 10, format)
    worksheet.set_column('F:F', 40, format)
    worksheet.set_column('G:G', 20, format)
    worksheet.set_column('H:H', 35, format)
    worksheet.set_column('E:E', 5, format)
    worksheet.set_column('A:A', 5, format)

writer.save()
