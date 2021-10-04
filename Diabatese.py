import pandas as pd
path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"
df = pd.read_csv(path)

print(df)
print(df.shape)

print(df.info())

print(df.describe())

missing_data = df.isnull()
print(missing_data.head(5))

a = missing_data.columns.values.tolist()
print(a)

for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")    

print(df)

#import libraries
import matplotlib.pyplot as plt
import seaborn as sns

labels= 'Diabetic','Not Diabetic'
plt.pie(df['Outcome'].value_counts(),labels=labels,autopct='%0.02f%%')
plt.legend()
plt.show()

