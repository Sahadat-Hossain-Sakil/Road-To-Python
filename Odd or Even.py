num = int(input('Enter a Number : '))
check = int(input(' Enter another number for check : '))

if num % 4 == 0 :
    print(num, 'is a multiple of 4 \n')
    print(num, 'is an even number')
elif num % 2 == 0 :
    print(num, 'is an even number')
else :
    print(num, 'is a odd number')

if num % check == 0 :
    print(num, 'divide evenly by', check)
else :
    print(num, 'is not divide evenly by', check)