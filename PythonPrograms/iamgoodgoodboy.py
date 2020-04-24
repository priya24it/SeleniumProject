import pandas as pd

strtext = "I am a good good boy"
df = pd.DataFrame(strtext)
print(df)
print(df.describe())
print(df.values)
print(df[0].value_counts())


