import pandas as pd

filePath = "filter.csv"
df = pd.read_csv(filePath)

print(df)

#Read Headers
# print(df.columns)

# Read Each Column 
# print(df['Name'])

#To read Top File Columns
#print(df['Name'][0:5])

#To Read Each Row first Row from CSV
# print(df.iloc[1])

for index, row in df.iterrows():
    
    #print(index, row)

    #To print only Specific Column ex. Name
    print(index, row['Name'])



#To Read First Four Row From CSV
# print(df.iloc[1:4])

