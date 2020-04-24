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

# Requete GET
resp = requests.get('https://jsonplaceholder.typicode.com/users?$top=1'
                    )
data = resp.text
data = data.replace('[','')
data = data.replace(']','')
data = str(data)
#print(data)
data = json.loads(json.dumps(resp.json()))

df = pd.DataFrame(data)
#print(df)




TotalColumns = list(df.shape)
d = {}
print(df.columns)
listofcolumns = df.columns.values.tolist()
for i in range(0,TotalColumns[1]):
    print(df[listofcolumns[i]].values)
    d[listofcolumns[i]] = df[listofcolumns[i]].values.tolist()

myDictionary = []
keys = ['id', 'address']
for key in keys:
    print(key)

myDictionary = d.copy()
del myDictionary['name']
del myDictionary['username']
del myDictionary['email']
del myDictionary['phone']
del myDictionary['website']

print(myDictionary)


#print(type(d))
#print(d['address'][1]['geo'])
#df1 = pd.DataFrame(d['address'][1]['geo'],index=[0])
#print(df1)
#print(df.df['address'].str.spilt(':'))
for k, v in d.items():
    print(k)
    print(str(v).replace('[',''))
    v = str(v).replace('[','')
    v = str(v).replace(']', '')
    d[k] = v
    #print(v)

print(d)



    # initialising_dictionary
ini_dict = {'geeks': {'Geeks': {'for': 7}},
            'for': {'geeks': {'Geeks': 3}},
            'Geeks': {'for': {'for': 1, 'geeks': 4}}}

#print("initial_dictionary", str(ini_dict))

# printing final dictionary

print("final_dictionary", str(convert_flatten(d)))




