#Exercise Question 8: Calculate total sale data for last year for each product and show it using a Pie chart
#Note: In Pie chart display Number of units sold per year for each product in percentage.

import pandas as pd
import matplotlib.pyplot as plt


#Read CSV File Data
df = pd.read_csv('company_sales_data.csv')

print(df)

#Get Month List
monthList = df['month_number'].tolist()

# print(monthList)

labels = ['FaceCream',  'FaceWash', 'ToothPaste', 'Bathing soap', 'Shampoo', 'Moisturizer']

#Sum Of Total Sales Products

salesData = [
            df['facecream'].sum(), df['facewash'].sum(),
            df['toothpaste'].sum(),  df['bathingsoap'].sum(),
            df['shampoo'].sum(), df['moisturizer'].sum()
]

plt.axis("equal")
plt.pie(salesData, labels=labels, autopct='%1.1f%%')
plt.legend(loc='lower right')
plt.title('Sales data')
plt.show()