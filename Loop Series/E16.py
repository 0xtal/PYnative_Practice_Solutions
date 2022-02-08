def cube(base) :
    return (base ** 3)


max = int(input('Give a number: ')) 
for i in range(1 ,max + 1) :
    print('Current Number is :', i, end = ' ')
    print('and the cube is', cube(i))