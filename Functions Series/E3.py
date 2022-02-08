def calculation(x, y) :
    sum = x + y
    diff = x - y
    return sum, diff


val1 = int(input('Enter first: '))
val2 = int(input('Enter second: '))
tot, min = calculation(val1, val2)
print('Sum:', tot, 'Diff:', min)