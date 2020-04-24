import openpyxl
import requests
import pandas as pd
import json
import ast
from collections import MutableMapping

import openpyxl
import requests
import pandas as pd
import json
import ast
from collections import MutableMapping


def convert_flatten(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k

        if isinstance(v, MutableMapping):
            items.extend(convert_flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

a = 4/2
#print(a)
b = 4//2
#print(b)

payload = {'api_key':'API_KEY_REMOVED'}

writer = pd.ExcelWriter('postmaninfo.xlsx')
# Requete GET
resp = requests.get('https://jsonplaceholder.typicode.com/users?$top=1'
                    )
data = resp.text
data = data.replace('[','')
data = data.replace(']','')
data = str(data)
data = json.loads(json.dumps(resp.json()))

df = pd.DataFrame(data)
TotalColumns = list(df.shape)

d = {}
listofcolumns = df.columns.values.tolist()

#print(listofcolumns)
for i in range(0,TotalColumns[1]):
    d[listofcolumns[i]] = df[listofcolumns[i]].values.tolist()

dfbasic = pd.DataFrame(d)
dfbasic = dfbasic.fillna(0)
print(dfbasic.columns)
totalnumberofrows = list(dfbasic.shape)
print('totla number of rows::',str(totalnumberofrows))



dfcmpany = pd.read_excel('json.xlsx')
dfcmpany = pd.DataFrame(dfcmpany)
print(dfcmpany.columns)
dffinal = pd.merge(left=dfbasic,right=dfcmpany,on='id', how='inner')
print(dffinal.shape)
dffinal.to_excel(writer,'company')

writer.save()