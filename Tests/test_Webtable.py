import pytest
from selenium import webdriver
import pandas as pd

@pytest.mark.usefixtures("setup")
#@pytest.mark.skip
class Test_Webtable:
    def test_accesswebtable(self):
       # sourceDF = pd.read_excel('merge.xlsx', sheet_name='sourceINSGrid')
        print('Open homepage..')
        rows = self.driver.find_elements_by_xpath("//table[@class ='dataTable']//tbody//tr")
        print("Number of rows" + str(len(rows)))
        columns = self.driver.find_elements_by_xpath("//table[@class ='dataTable']//tbody//tr[1]//td")
        print("Number of rows" + str(len(columns)))
        #rows = self.driver.find_element_by_xpath("//table[@class ='dataTable']//tbody//tr/td[1][1]").text
        #print(rows)
        Dict = {}
        l1 = []

        for column in range(1,len(columns)+1):
            l1 = "k" + str([column])
            l1 = []
            columnvalue = self.driver.find_element_by_xpath("//table[@class ='dataTable']//thead//th[" + str(column) + "]")
           # print(columnvalue.text)
            for row in range(1,len(rows)+1):
                rowvalue = self.driver.find_element_by_xpath("//table[@class ='dataTable']//tbody//tr["+str(row)+"]//td["+str(column)+"]")
                l1.append(rowvalue.text)
            print(l1)
           # Dict[rowvalue] = l1
            Dict[columnvalue.text] =  l1

        self.driver.close()

        #print(Dict)
        df =pd.DataFrame(Dict)
        print(df.columns)
        print(df.describe())
        df = df[df['Current Price (Rs)'] == (df['Current Price (Rs)'].max())]
        print(df)
        df.to_excel("webtable.xlsx")


        #print(len(rows))
       # for row in range(0,len(rows)):
            #print(rows[row].text)
        #    l1 = list(rows[row].text)
         #   print(l1)
      #  columns = self.driver.find_elements_by_xpath("//table[@class ='dataTable']//tbody//tr/td")
       # print(columns)

        #for i in range(0,len(columns)):
         #   print(i.text)





