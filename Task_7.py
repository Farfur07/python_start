def getSum(n):

    sum = 0
    for digit in str(n):
        sum += int(digit)
        return sum

n = input('Enter number: ')
print('Sum of digits: ', getSum(n))
