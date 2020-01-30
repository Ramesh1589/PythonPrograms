number = int(input('Enter a number of row: ' ))

for row in range(1, number):
    for column in range(1, row + 1):
        print(column, end= "")
    print("")    

#Output
# 1
# 12
# 123
# 1234
# 12345
# 123456
# 1234567
# 12345678    