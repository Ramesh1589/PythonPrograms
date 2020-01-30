import pandas as pd
import smtplib


file_path = 'sample.xlsx'

df = pd.read_excel(file_path)

# print(df)

unique_city = df['city'].unique()

print(unique_city)

for city  in unique_city:
    df1 =  df[df['city'] == city]
    output_file_name = str(city) + '_Training.xlsx'
    df1.to_excel('excel/' + output_file_name, index = False)

