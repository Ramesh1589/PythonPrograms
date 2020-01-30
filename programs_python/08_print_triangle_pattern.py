number = int(input('Enter a number of row: ' ))
for num in range(number):
    for i in range(num):
        #print (num, end=" ") #print number
        print (num, end=" ") #print star
    # new line after each row to display pattern correctly
    print("\n")

#Output
 
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# * * * * * * *
# * * * * * * * *
# * * * * * * * * *    