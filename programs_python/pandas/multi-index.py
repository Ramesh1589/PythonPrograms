
import pandas as pd

filePath = 'multiindex.csv'

df = pd.read_csv(filePath)

# print(df)

#       Date   Close    Volume Symbol
# 0  2016-10-03   31.50  14070500   CSCO
# 1  2016-10-03  112.52  21701800   AAPL
# 2  2016-10-03   57.42  19189500   MSFT
# 3  2016-10-04  113.00  29736800   AAPL
# 4  2016-10-04   57.24  20085900   MSFT
# 5  2016-10-04   31.35  18460400   CSCO
# 6  2016-10-05   57.64  16726400   MSFT
# 7  2016-10-05   31.59  11808600   CSCO
# 8  2016-10-05  113.05  21453100   AAPL

# df = df.groupby(['Symbol', 'Date']).Close.mean()

# print(df)

# Symbol  Date
# AAPL    2016-10-03    112.52
#         2016-10-04    113.00
#         2016-10-05    113.05
# CSCO    2016-10-03     31.50
#         2016-10-04     31.35
#         2016-10-05     31.59
# MSFT    2016-10-03     57.42
#         2016-10-04     57.24
#         2016-10-05     57.64

# df = df.unstack()

# print(df)

# Date    2016-10-03  2016-10-04  2016-10-05
# Symbol
# AAPL        112.52      113.00      113.05
# CSCO         31.50       31.35       31.59
# MSFT         57.42       57.24       57.64

# Reposition Symbol Column at initial Column


df.set_index(['Symbol', 'Date'], inplace=True)

# print(df)
                        
# Symbol Date         Close  Volume
# CSCO   2016-10-03   31.50  14070500
# AAPL   2016-10-03  112.52  21701800
# MSFT   2016-10-03   57.42  19189500
# AAPL   2016-10-04  113.00  29736800
# MSFT   2016-10-04   57.24  20085900
# CSCO   2016-10-04   31.35  18460400
# MSFT   2016-10-05   57.64  16726400
# CSCO   2016-10-05   31.59  11808600
# AAPL   2016-10-05  113.05  21453100


#Sorting Data frame with multiindex
df.sort_index(inplace=True)

print(df)

# Symbol  Date        Close   Volume
# AAPL   2016-10-03  112.52  21701800
#        2016-10-04  113.00  29736800
#        2016-10-05  113.05  21453100
# CSCO   2016-10-03   31.50  14070500
#        2016-10-04   31.35  18460400
#        2016-10-05   31.59  11808600
# MSFT   2016-10-03   57.42  19189500
#        2016-10-04   57.24  20085900
#        2016-10-05   57.64  16726400


#Search Data Using Symbol column
# output = df.loc['AAPL']

# print(output)

# Date         Close    Volume
# 2016-10-03  112.52  21701800
# 2016-10-04  113.00  29736800
# 2016-10-05  113.05  21453100

#FILTER DATA WITH SYMBOL AND DATE  
# : for all columns and for specific column replace : ==> ('column name') 

# otuput = df.loc[('AAPL', '2016-10-03'), :]

# print(otuput)

# Close          112.52
# Volume    21701800.0


# Filter Data With Multiple Symbols and Date

# otuput = df.loc[(['AAPL', 'MSFT'], '2016-10-03'), :]

# print(otuput)
                 
# Symbol Date        Close    Volume 
# AAPL   2016-10-03  112.52  21701800
# MSFT   2016-10-03   57.42  19189500

#Filter Data With Multiple Date and Symbol

# otuput = df.loc[(['AAPL'], ['2016-10-03', '2016-10-04']), :]

# print(otuput)

# Symbol Date        Close   Volume
# AAPL   2016-10-03  112.52  21701800
#        2016-10-04  113.00  29736800