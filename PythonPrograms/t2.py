import pandas as pd

#df = pd.read_json(r'file.json',lines=True)
#df = pd.DataFrame()


j = """
{"A":1,"B":4}

{"A":2,"B":5}
"""
df = pd.read_json(j, lines=True)
df = pd.DataFrame(df)
print(df)


j1 = { "id": 1, "name": "Leanne Graham", "username": "Bret", "email": "Sincere@april.biz" }
print(type(j1))
df = pd.read_json(j1, lines=True)
df = pd.DataFrame(df)
print(df)