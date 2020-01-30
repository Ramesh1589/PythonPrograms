import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv('company_sales_data.csv')

print(df)
#Get Total Profit List
profitList = df['total_profit'].tolist()

#Get Total Month Numbers
monthList = df['month_number'].tolist()

# print("Total Profit List", profitList)
# print("All month list",monthList)

plt.plot(monthList, profitList, label = "Month-wise Profit Data of Last Year")

plt.xlabel('Month Number')

plt.ylabel('Profit in Dollars')

plt.xticks(monthList)

plt.title('Company Profit per Month')

plt.yticks([100000, 200000, 300000, 400000, 500000])

plt.show()