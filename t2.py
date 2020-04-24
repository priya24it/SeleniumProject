import requests
import pandas as pd
import json
import ast


def flatten_dict(dd, separator ='_', prefix =''):
    return { prefix + separator + k if prefix else k : v
             for kk, vv in dd.items()
             for k, v in flatten_dict(vv, separator, kk).items()
             } if isinstance(dd, dict) else { prefix : dd }


#resp = requests.get('https://api.exchangeratesapi.io/latest?symbols=USD,GBP')
resp = requests.get('https://jsonplaceholder.typicode.com/users?$top=1')
print(resp.status_code)
d = json.loads(resp.text)
print(type(d))
#print(d)

#d= str(d)
#d = d.replace('[','')
#d = d.replace(']','')

print(d[1:len(d)])
#print(d)
# priniting initial dictionary
#print("initial_dictionary", str(d))

# printing final dictionary
print("final_dictionary", str(flatten_dict(d)))