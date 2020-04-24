import pandas as pd
import numpy as np

class TestData:

    def testData(self):
        sourceDF = pd.read_excel('DDT.xlsx')
        sourceDF = pd.DataFrame(sourceDF)
        TotalColumns = list(sourceDF.shape)
        d = {}
        print(sourceDF.columns)
        listofcolumns = sourceDF.columns.values.tolist()
        for i in range(0,TotalColumns[1]):
            d[listofcolumns[i]] = sourceDF[listofcolumns[i]].values.tolist()
        return d


