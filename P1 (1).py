'''Problem 1: Find the factorial of the given number'''
num = int(input('Enter a number: '))
fact = 1
if(num < 0):
    print('Not defined')
else:
    while(num > 0):
        fact = fact * num
        num = num - 1
    print(fact)
