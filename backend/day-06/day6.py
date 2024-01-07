limit = int(input('Limit: '))

for i in range(1, limit):
    printable = ''
    
    if (i % 3 == 0 and i % 5 == 0):
        printable = 'FizzBuzz'
    elif (i % 3 == 0):
        printable = 'Fizz'
    elif (i % 5 == 0):
        printable = 'Buzz'
    else:
        printable = i

    print(printable)
