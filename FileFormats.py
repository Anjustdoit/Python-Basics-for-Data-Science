import pandas as pd
import pandas as pd
import numpy as np

url ='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv'
df = pd.read_csv(url)
df.columns =['First Name', 'Last Name', 'Location ', 'City','State','Area Code']


df = df[['First Name', 'Last Name', 'Location ', 'City','State','Area Code']]
print(df)

print(df.loc[0])
print(df.loc[[0,1,2], "First Name" ])

print(df.iloc[[0,1,2], 0])

df1=pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])


df1 = df1.transform(func = lambda x : x + 10)
print(df1)

result = df1.transform(func = ['sqrt'])
print(result)
print(df1)