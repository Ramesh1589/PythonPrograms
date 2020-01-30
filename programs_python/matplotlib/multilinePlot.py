#Exercise Question 3: Read all product sales data and show it  using a multiline plot
# Display the number of units sold per month for each product using multiline plots. (i.e., Separate Plotline for each product for each product).

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('company_sales_data.csv')

print(df)

monthList = df['month_number'].tolist()

# print("Month List", monthList)

faceCreamSalesData = df['facecream'].tolist()

# print("Face cream List Data", faceCreamSalesData)

faceWashSalesData = df['facewash'].tolist()

# print("Face wash List Data", faceWashSalesData)

toothPasteSalesData = df['toothpaste'].tolist()

# print("Tooth Past List Data", toothPasteSalesData)

bathingSoapSalesData = df['bathingsoap'].tolist()

shampooSalesData =  df['shampoo'].tolist()


plt.plot(monthList, faceCreamSalesData,   label = "Face Cream Sales Data",  marker= 'o', linewidth= 3)

plt.plot(monthList, faceWashSalesData,    label = "Face Wash Sales Data",   marker= 'o', linewidth= 3)

plt.plot(monthList, toothPasteSalesData,  label = "Toothpest Sales Data",    marker= 'o', linewidth= 3)

plt.plot(monthList, bathingSoapSalesData, label = "Bathing soap Sales Data", marker= 'o', linewidth= 3)

plt.plot(monthList, shampooSalesData,     label = "Shampoo Sales Data", marker= 'o', linewidth= 3)


plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.legend(loc='upper left')
plt.xticks(monthList)
plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])
plt.title('Sales data')
plt.show()
