import pandas as pd


# file_path = 'sample.xlsx'


df = pd.read_csv('Automobile_data.csv')

#Top five Record

# print(df.head(5))

#Last Five Record

# print(df.tail(5))

#Find the most expensive car company name
# df = df[['company', 'price']][df.price == df['price'].max()]
# print(df)


#Question 4: Print All Toyota Cars details
# carManufacturer = df.groupby('company')
# car = carManufacturer.get_group('isuzu')
# final = car.dropna()
# print(car)

# Question 5: Count total cars per company
# counts = df['company'].value_counts()
# print(counts)

#Question 6: Find each company’s Higesht price car
# manufacture = df.groupby('company')
# car = manufacture['company', 'price', 'body-style'].max()
# print(car)

# Question 7: Find the average mileage of each car making company
# cars = df.groupby('company')
# avg = cars['company', 'average-mileage'].mean()
# print(avg)


# Question 8: Sort all cars by Price column
# cars = df.sort_values(by=['price'], ascending=False)
# print(cars.head(5))