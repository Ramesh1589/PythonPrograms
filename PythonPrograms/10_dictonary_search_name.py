# Program To Create Dictonary with key value and search name form Dictonary.

n = int(input('Enter number of students ::'))

d = {}

for i in range(n):

    name =  input('Enter student name :: ')
  
    marks = input('Enter student marks :: ')

    d[name] =  marks

while True:

    name = input('Enter student name to be search :: ') 

    marks = d.get(name, -1)

    if marks == -1:

        print('sorry Student not found....')

    else:

        print("Marks of", name , "is", marks )

    options = input(' Do you want to continue [ Yes | No ] ::')

    if options == 'No':
        
        break

print('Thank you using Application...')